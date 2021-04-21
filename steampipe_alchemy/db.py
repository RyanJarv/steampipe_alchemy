from typing import TypeVar, Iterable, Union, Any, Generic

import sqlmypy

import sqlalchemy.orm
import sqlalchemy.future
from sqlalchemy.orm import Query

from steampipe_alchemy.base import engine

Session: sqlalchemy.orm.sessionmaker = sqlalchemy.orm.sessionmaker(engine, future=True)
db: sqlalchemy.orm.Session = Session()

T = TypeVar('T')

class Q(Generic[T], Query):
    """Wrapper around sqlalchemy.orm.Query that supports type annotations.

    The Query object can be used as it self or as an iterable over the model. When used as an iterable it does not
    provide autocomplete of the underlying class by default.

    i.e.
        for i in sess.query(Model).all():
            ...

    Here i will be an object of type Model but because of the dynamic nature of sqlalchemy we need to add a type hint to
    get completion to work correctly.

        i:  Model

    Putting this everywhere is kinda a pain though, so instead this class can be used with a custom query method (below) to
    automatically set the right type.
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

    def with_for_update(self, read=False, nowait=False, of=None, skip_locked=False, key_share=False) -> Union[Iterable[T], 'Q']:
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



