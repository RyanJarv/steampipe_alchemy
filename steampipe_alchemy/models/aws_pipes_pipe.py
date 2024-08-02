from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsPipesPipe(Base, FormatMixins):
    __tablename__ = 'aws_pipes_pipe'
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    enrichment_parameters = Column('enrichment_parameters', JSON, nullable=True)
    target_parameters = Column('target_parameters', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    source_prefix = Column('source_prefix', Text, nullable=True)
    state_reason = Column('state_reason', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    target_prefix = Column('target_prefix', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    target = Column('target', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    current_state = Column('current_state', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    desired_state = Column('desired_state', Text, nullable=True)
    enrichment = Column('enrichment', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    source = Column('source', Text, nullable=True)