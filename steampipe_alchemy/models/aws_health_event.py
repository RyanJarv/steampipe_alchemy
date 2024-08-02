from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsHealthEvent(Base, FormatMixins):
    __tablename__ = 'aws_health_event'
    last_updated_time = Column('last_updated_time', TIMESTAMP, nullable=True)
    end_time = Column('end_time', TIMESTAMP, nullable=True)
    start_time = Column('start_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    status_code = Column('status_code', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    service = Column('service', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    event_scope_code = Column('event_scope_code', Text, nullable=True)
    event_type_category = Column('event_type_category', Text, nullable=True)
    event_type_code = Column('event_type_code', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)