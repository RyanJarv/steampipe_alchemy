import json
import os
import subprocess
import atexit
import sys
import tarfile
import urllib.request
import zipfile
from pathlib import Path

from typing import TypeVar, Iterable, Union, Generic, List, Optional
from typing_extensions import TypedDict
from enum import Enum

from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import MetaData, create_engine, orm
from dataclasses import dataclass

from steampipe_alchemy.utils import deprecated

metadata = MetaData()
Base: 'DeclarativeMeta' = declarative_base(metadata=metadata)

T = TypeVar('T')


class Query(Generic[T], orm.Query):
    """Wrapper around sqlalchemy.orm.Query that supports type annotations.

    The Query object can be used as it self or as an iterable over the model. When used as an iterable
    it does not provide autocomplete of the underlying class by default.
    i.e.
        for i in sess.query(Model).all():
            ...

    Here i will be an object of type Model but because of the dynamic nature of sqlalchemy we need to
    add a type hint to get completion to work correctly.

        i:  Model

    Putting this everywhere is kinda a pain though, so instead this class can be used with a custom
    query method (below) to automatically set the right type.
    """
    ...

    def all(self) -> Union[Iterable[T], 'Query']:
        ...

    def _set_lazyload_from(self, state) -> Union[Iterable[T], 'Query']:
        ...

    def limit(self, limit: int) -> Union[Iterable[T], 'Query']:
        ...

    def where(self, *criterion) -> Union[Iterable[T], 'Query']:
        ...

    def filter(self, *criterion) -> Union[Iterable[T], 'Query']:
        ...

    def only_return_tuples(self, value) -> Union[Iterable[T], 'Query']:
        ...

    def enable_eagerloads(self, value) -> Union[Iterable[T], 'Query']:
        ...

    def enable_assertions(self, value) -> Union[Iterable[T], 'Query']:
        ...

    def _with_current_path(self, path) -> Union[Iterable[T], 'Query']:
        ...

    def yield_per(self, count) -> Union[Iterable[T], 'Query']:
        ...

    def correlate(self, *fromclauses) -> Union[Iterable[T], 'Query']:
        ...

    def autoflush(self, setting) -> Union[Iterable[T], 'Query']:
        ...

    def populate_existing(self) -> Union[Iterable[T], 'Query']:
        ...

    def _with_invoke_all_eagers(self, value) -> Union[Iterable[T], 'Query']:
        ...

    def add_entity(self, entity, alias=None) -> Union[Iterable[T], 'Query']:
        ...

    def with_session(self, session) -> Union[Iterable[T], 'Query']:
        ...

    def _set_enable_single_crit(self, val) -> Union[Iterable[T], 'Query']:
        ...

    def _from_selectable(self, fromclause, set_entity_from=True) -> Union[Iterable[T], 'Query']:
        ...

    def with_entities(self, *entities) -> Union[Iterable[T], 'Query']:
        ...

    def add_columns(self, *column) -> Union[Iterable[T], 'Query']:
        ...

    def options(self, *args) -> Union[Iterable[T], 'Query']:
        ...

    def execution_options(self, **kwargs) -> Union[Iterable[T], 'Query']:
        ...

    def with_for_update(self, read=False, nowait=False, of=None, skip_locked=False, key_share=False) -> \
            Union[Iterable[T], 'Query']:
        ...

    def params(self, *args, **kwargs) -> Union[Iterable[T], 'Query']:
        ...

    def order_by(self, *clauses) -> Union[Iterable[T], 'Query']:
        ...

    def group_by(self, *clauses) -> Union[Iterable[T], 'Query']:
        ...

    def having(self, criterion) -> Union[Iterable[T], 'Query']:
        ...

    def join(self, target, *props, **kwargs) -> Union[Iterable[T], 'Query']:
        ...

    def reset_joinpoint(self) -> Union[Iterable[T], 'Query']:
        ...

    def select_from(self, *from_obj) -> Union[Iterable[T], 'Query']:
        ...

    def select_entity_from(self, from_obj) -> Union[Iterable[T], 'Query']:
        ...

    def slice(self, start, stop) -> Union[Iterable[T], 'Query']:
        ...

    def offset(self, offset) -> Union[Iterable[T], 'Query']:
        ...

    def distinct(self, *expr) -> Union[Iterable[T], 'Query']:
        ...

    def from_statement(self, statement) -> Union[Iterable[T], 'Query']:
        ...


AwsConfig = TypedDict('AwsConfig', {
    "regions": List[str],
    "profile": str,
})


class UnexpectedStateException(Exception):
    pass


class ServiceState(Enum):
    UNKNOWN = 0
    STOPPED = 1
    RUNNING = 2


@dataclass()
class ServiceStatus:
    state: ServiceState = ServiceState.UNKNOWN
    reason: str = ""


class SteamPipe:
    home_dir = Path('~/.local/share/steampipe_alchemy').expanduser().absolute()
    bin_dir = Path('~/.local/share/steampipe_alchemy/bin').expanduser().absolute()

    def __init__(self):
        self.config = Path(self.home_dir / 'config/aws.spc')

        self.engine: Optional['engine.Engine'] = None
        self.db: Optional['orm.session.Session'] = None
        self.Session: Optional['orm.sessionmaker'] = None
        self.database_conn: Optional[str] = None
        self._status: ServiceStatus = ServiceStatus()

        self.status()

    def query(self, resource: T) -> Union[Iterable[T], Query[T]]:
        """Wrapper around Session.query that supports type annotations."""
        if not self.db:
            raise UnexpectedStateException("Steampipe must be in the started state to call this function.")
        return self.db.query(resource)

    def update_config(self, aws: Optional[AwsConfig] = None, **kwargs):
        if aws:
            kwargs['aws'] = aws

        config = ""
        for name, conf in kwargs.items():
            config += f"""
                connection "{name}" {{
                    {os.linesep.join((f'{k} = {json.dumps(v)}' for k, v in conf.items()))}
                }}
            """
        self.config.write_text(config)

        if self._status == ServiceState.RUNNING:
            self.restart()

    def status(self) -> ServiceStatus:
        if not (self.bin_dir/'steampipe').is_file():
            self._status = ServiceStatus(
                state=ServiceState.UNKNOWN,
                reason=f"[WARN] Could not find the steampipe binary at {self.bin_dir}"
            )
            return self._status

        out = subprocess.check_output([self.bin_dir/'steampipe', 'service', 'status', '--install-dir',
                                       str(self.home_dir)])
        if b'NOT running' in out:
            self._status = ServiceStatus(
                state=ServiceState.STOPPED,
                reason=out,
            )
        elif b'service is now running' in out:
            self.set_db(out)
            self._status = ServiceStatus(
                state=ServiceState.RUNNING,
                reason=out,
            )
        else:
            self._status = ServiceStatus(
                state=ServiceState.UNKNOWN,
                reason=f"steampipe is in an unknown state: {out}"
            )
        return self._status

    def restart(self):
        self.stop()
        self.start()

    def set_db(self, status_out: bytes):
        self.database_conn = list(filter(lambda l: b'postgres://steampipe' in l, status_out.splitlines()))
        self.database_conn = self.database_conn[0].decode().strip()

        # sqlalchemy expects postgresql:// rather then postgres://
        database_conn = self.database_conn.replace('postgres', 'postgresql')

        self.engine = create_engine(database_conn)
        self.Session = orm.sessionmaker(self.engine)
        self.db = self.Session()

    def start(self, **kwargs) -> ServiceStatus:
        if self.status().state == ServiceState.RUNNING:
            print("[WARN] Steampipe was running when we tried to start it. This is most likely a orphaned session. "
                  "It will be shutdown when we exit.", file=sys.stderr)
            return self._status
        else:
            try:
                out = subprocess.check_output([str(self.bin_dir/'steampipe'), 'service', 'start', '--install-dir',
                                               str(self.home_dir), '--database-listen', 'local'],
                                              env={**os.environ, **kwargs})
            except subprocess.CalledProcessError as e:
                raise UnexpectedStateException(ServiceStatus(
                    reason=f"Stdout: {str(e.stdout)}\nStderr: {str(e.stderr)}", state=ServiceState.UNKNOWN))
            except FileNotFoundError as e:
                raise UnexpectedStateException(ServiceStatus(
                    reason=f"No steampipe binary found at '{e.filename}'", state=ServiceState.UNKNOWN))
            status = self.status()
            if status.state != ServiceState.RUNNING:
                status.reason = f"Output of starting steampipe: {str(out)}\n\n" + \
                                f"Output of checking status: {status.reason}\n\n"
                raise UnexpectedStateException(status)
        atexit.register(self.stop)
        return self._status

    def stop(self):
        subprocess.check_output([self.bin_dir / 'steampipe', 'service', 'stop', '--install-dir', str(self.home_dir),
                                 '--force'])

    def install(self, plugins: List[str] = []):
        os.makedirs(self.bin_dir, exist_ok=True)
        if os.uname().sysname == 'Darwin':
            self.get_darwin()
        elif os.uname().sysname == 'Linux':
            self.get_linux()
        os.chmod(self.bin_dir / 'steampipe', mode=0o0775)

        for plugin in plugins:
            self.install_plugin(plugin)

    def install_plugin(self, plugin: str):
        subprocess.check_output([
            self.bin_dir / 'steampipe', 'plugin', 'install', '--install-dir', str(self.home_dir), plugin])

    @staticmethod
    def get_latest() -> str:
        resp = urllib.request.urlopen('https://api.github.com/repos/turbot/steampipe/releases/latest')
        resp = json.loads(resp.read())
        return resp['name']

    def get_linux(self):
        uri = f"https://github.com/turbot/steampipe/releases/download/{self.get_latest()}/steampipe_linux_amd64.tar.gz"
        resp = urllib.request.urlopen(uri)

        with open(self.bin_dir / 'steampipe.tar.gz', 'wb') as f:
            f.write(resp.read())

        with tarfile.open(self.bin_dir / 'steampipe.tar.gz', 'r') as z:
            z.extractall(self.bin_dir)

    def get_darwin(self):
        uri = f"https://github.com/turbot/steampipe/releases/download/{self.get_latest()}/steampipe_darwin_amd64.zip"
        resp = urllib.request.urlopen(uri)

        with open(self.bin_dir / 'steampipe.zip', 'wb') as f:
            f.write(resp.read())

        with zipfile.ZipFile(self.bin_dir / 'steampipe.zip', 'r') as z:
            z.extractall(self.bin_dir)


# !! The functions below where deprecated in favor of the SteamPipe class
steam: Optional[SteamPipe] = None


@deprecated
def query(*args, **kwargs):
    global steam
    if not steam:
        steam = SteamPipe()
    print(steam)
    resp = steam.query(*args, **kwargs)
    print(resp)
    return resp


@deprecated
def update_config(*args, **kwargs):
    global steam
    if not steam:
        steam = SteamPipe()
    return steam.update_config(*args, **kwargs)


@deprecated
def install(*args, **kwargs):
    global steam
    if not steam:
        steam = SteamPipe()
    return steam.install(*args, **kwargs)


@deprecated
def start(**kwargs) -> ServiceStatus:
    global steam
    if not steam:
        steam = SteamPipe()
    resp = steam.start(**kwargs)
    return resp


@deprecated
def stop():
    global steam
    if not steam:
        steam = SteamPipe()
    return steam.stop()


@deprecated
def install_plugin(*args, **kwargs):
    global steam
    if not steam:
        steam = SteamPipe()
    return steam.install_plugin(*args, **kwargs)
