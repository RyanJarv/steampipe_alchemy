"""Top-level package for steampipe-alchemy."""

__author__ = """Ryan Gerstenkorn"""
__email__ = 'ryan.gerstenkorn@rhinosecuritylabs.com'
__version__ = '0.1.0'

from typing import TypeVar, Iterable, Union, Iterator, List, Sequence

import sqlalchemy.orm
import sqlalchemy.future
from sqlalchemy.orm import Query

from steampipe_alchemy.base import engine

Session: 'sqlalchemy.orm.sessionmaker' = sqlalchemy.orm.sessionmaker(engine, future=True)
db: 'sqlalchemy.orm.Session' = Session()

T = TypeVar('T')


def query(resource: T) -> Union[Iterable[T], Query]:
    """Wrapper around Session.query that supports type annotations."""
    return db.query(resource)
