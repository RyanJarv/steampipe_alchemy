from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlueConnection(Base, FormatMixins):
    __tablename__ = 'aws_glue_connection'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    last_updated_time = Column('last_updated_time', TIMESTAMP, nullable=True)
    connection_properties = Column('connection_properties', JSON, nullable=True)
    match_criteria = Column('match_criteria', JSON, nullable=True)
    physical_connection_requirements = Column('physical_connection_requirements', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    connection_type = Column('connection_type', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    last_updated_by = Column('last_updated_by', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)