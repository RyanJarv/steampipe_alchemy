import json
import os
import subprocess
import atexit
import tarfile
import urllib.request
import zipfile
from pathlib import Path

from typing import TypeVar, Iterable, Union, Generic, List, Optional

import sqlalchemy.orm
import sqlalchemy.future
from sqlalchemy import MetaData
from sqlalchemy.future import Engine, create_engine
from sqlalchemy.orm import Query, declarative_base, DeclarativeMeta

metadata = MetaData()
Base: 'DeclarativeMeta' = declarative_base(metadata=metadata)

DATABASE_CONNECTION_PATH: Optional[str] = None
engine: Optional[Engine] = None

T = TypeVar('T')


class Q(Generic[T], Query):
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

    def _set_lazyload_from(self, state) -> Union[Iterable[T], 'Q']:
        ...

    def limit(self, limit: int) -> Union[Iterable[T], 'Q']:
        ...

    def where(self, *criterion) -> Union[Iterable[T], 'Q']:
        ...

    def filter(self, *criterion) -> Union[Iterable[T], 'Q']:
        ...

    def only_return_tuples(self, value) -> Union[Iterable[T], 'Q']:
        ...

    def enable_eagerloads(self, value) -> Union[Iterable[T], 'Q']:
        ...

    def enable_assertions(self, value) -> Union[Iterable[T], 'Q']:
        ...

    def _with_current_path(self, path) -> Union[Iterable[T], 'Q']:
        ...

    def yield_per(self, count) -> Union[Iterable[T], 'Q']:
        ...

    def correlate(self, *fromclauses) -> Union[Iterable[T], 'Q']:
        ...

    def autoflush(self, setting) -> Union[Iterable[T], 'Q']:
        ...

    def populate_existing(self) -> Union[Iterable[T], 'Q']:
        ...

    def _with_invoke_all_eagers(self, value) -> Union[Iterable[T], 'Q']:
        ...

    def add_entity(self, entity, alias=None) -> Union[Iterable[T], 'Q']:
        ...

    def with_session(self, session) -> Union[Iterable[T], 'Q']:
        ...

    def _set_enable_single_crit(self, val) -> Union[Iterable[T], 'Q']:
        ...

    def _from_selectable(self, fromclause, set_entity_from=True) -> Union[Iterable[T], 'Q']:
        ...

    def with_entities(self, *entities) -> Union[Iterable[T], 'Q']:
        ...

    def add_columns(self, *column) -> Union[Iterable[T], 'Q']:
        ...

    def options(self, *args) -> Union[Iterable[T], 'Q']:
        ...

    def execution_options(self, **kwargs) -> Union[Iterable[T], 'Q']:
        ...

    def with_for_update(self, read=False, nowait=False, of=None, skip_locked=False, key_share=False) -> \
            Union[Iterable[T], 'Q']:
        ...

    def params(self, *args, **kwargs) -> Union[Iterable[T], 'Q']:
        ...

    def order_by(self, *clauses) -> Union[Iterable[T], 'Q']:
        ...

    def group_by(self, *clauses) -> Union[Iterable[T], 'Q']:
        ...

    def having(self, criterion) -> Union[Iterable[T], 'Q']:
        ...

    def join(self, target, *props, **kwargs) -> Union[Iterable[T], 'Q']:
        ...

    def reset_joinpoint(self) -> Union[Iterable[T], 'Q']:
        ...

    def select_from(self, *from_obj) -> Union[Iterable[T], 'Q']:
        ...

    def select_entity_from(self, from_obj) -> Union[Iterable[T], 'Q']:
        ...

    def slice(self, start, stop) -> Union[Iterable[T], 'Q']:
        ...

    def offset(self, offset) -> Union[Iterable[T], 'Q']:
        ...

    def distinct(self, *expr) -> Union[Iterable[T], 'Q']:
        ...

    def from_statement(self, statement) -> Union[Iterable[T], 'Q']:
        ...


def query(resource: T) -> Union[Iterable[T], Q[T]]:
    """Wrapper around Session.query that supports type annotations."""
    return db.query(resource)


home_dir = Path('~/.local/share/steampipe_alchemy').expanduser().absolute()
bin_dir = Path('~/.local/share/steampipe_alchemy/bin').expanduser().absolute()


def update_config(aws_regions: List[str]):
    Path(home_dir / 'config/aws.spc').write_text(f"""
        connection "aws" {{
            plugin = "aws"
            regions = {str(aws_regions).replace("'", '"')}
        }}
    """)


def start(**kwargs):
    global engine, Session, db
    out = subprocess.check_output(
        [bin_dir / 'steampipe', 'service', 'start', '--install-dir', str(home_dir), '--database-listen', 'local'],
        env={**os.environ, **kwargs},
    )
    atexit.register(stop)

    DATABASE_CONNECTION_PATH = list(filter(lambda l: b'postgres://steampipe' in l, out.splitlines()))
    DATABASE_CONNECTION_PATH = DATABASE_CONNECTION_PATH[0].decode().strip()

    # sqlalchemy expects postgresql:// rather then postgres://
    DATABASE_CONNECTION_PATH = DATABASE_CONNECTION_PATH.replace('postgres', 'postgresql')

    engine = create_engine(DATABASE_CONNECTION_PATH)
    Session = sqlalchemy.orm.sessionmaker(engine, future=True)
    db = Session()


def stop():
    subprocess.check_output([bin_dir / 'steampipe', 'service', 'stop', '--install-dir', str(home_dir), '--force'])


def get_latest() -> str:
    resp = urllib.request.urlopen('https://api.github.com/repos/turbot/steampipe/releases/latest')
    resp = json.loads(resp.read())
    return resp['name']


def install(plugins: List[str]):
    os.makedirs(bin_dir, exist_ok=True)
    if os.uname().sysname == 'Darwin':
        get_darwin()
    elif os.uname().sysname == 'Linux':
        get_linux()
    os.chmod(bin_dir / 'steampipe', mode=0o0775)

    for plugin in plugins:
        install_plugin(plugin)


def install_plugin(plugin: str):
    subprocess.check_output([bin_dir / 'steampipe', 'plugin', 'install', '--install-dir', str(home_dir), plugin])


def get_linux():
    ver = get_latest()
    uri = f"https://github.com/turbot/steampipe/releases/download/{ver}/steampipe_linux_amd64.tar.gz"
    resp = urllib.request.urlopen(uri)

    with open(bin_dir / 'steampipe.tar.gz', 'wb') as f:
        f.write(resp.read())

    with tarfile.TarFile(bin_dir / 'steampipe.tar.gz', 'r') as z:
        z.extractall(bin_dir)


def get_darwin():
    ver = get_latest()
    uri = f"https://github.com/turbot/steampipe/releases/download/{ver}/steampipe_darwin_amd64.zip"
    resp = urllib.request.urlopen(uri)

    with open(bin_dir / 'steampipe.zip', 'wb') as f:
        f.write(resp.read())

    with zipfile.ZipFile(bin_dir / 'steampipe.zip', 'r') as z:
        z.extractall(bin_dir)
