from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodecommitRepository(Base, FormatMixins):
    __tablename__ = 'aws_codecommit_repository'
    last_modified_date = Column('last_modified_date', TIMESTAMP, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    default_branch = Column('default_branch', Text, nullable=True)
    repository_name = Column('repository_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    repository_id = Column('repository_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    clone_url_http = Column('clone_url_http', Text, nullable=True)
    clone_url_ssh = Column('clone_url_ssh', Text, nullable=True)