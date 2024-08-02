from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSfnStateMachine(Base, FormatMixins):
    __tablename__ = 'aws_sfn_state_machine'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    logging_configuration = Column('logging_configuration', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tracing_configuration = Column('tracing_configuration', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    definition = Column('definition', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)