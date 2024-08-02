from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodeartifactRepository(Base, FormatMixins):
    __tablename__ = 'aws_codeartifact_repository'
    _ctx = Column('_ctx', JSON, nullable=True)
    external_connections = Column('external_connections', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    repository_endpoint = Column('repository_endpoint', JSON, nullable=True)
    upstreams = Column('upstreams', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    administrator_account = Column('administrator_account', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    domain_owner = Column('domain_owner', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)