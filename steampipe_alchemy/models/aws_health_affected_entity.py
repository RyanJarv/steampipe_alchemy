from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsHealthAffectedEntity(Base, FormatMixins):
    __tablename__ = 'aws_health_affected_entity'
    _ctx = Column('_ctx', JSON, nullable=True)
    last_updated_time = Column('last_updated_time', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    status_code = Column('status_code', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    entity_url = Column('entity_url', Text, nullable=True)
    entity_value = Column('entity_value', Text, nullable=True)
    event_arn = Column('event_arn', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)