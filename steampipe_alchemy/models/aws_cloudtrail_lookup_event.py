from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudtrailLookupEvent(Base, FormatMixins):
    __tablename__ = 'aws_cloudtrail_lookup_event'
    event_time = Column('event_time', TIMESTAMP, nullable=True)
    end_time = Column('end_time', TIMESTAMP, nullable=True)
    start_time = Column('start_time', TIMESTAMP, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    cloud_trail_event = Column('cloud_trail_event', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    event_id = Column('event_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    username = Column('username', Text, nullable=True)
    event_name = Column('event_name', Text, nullable=True)
    event_source = Column('event_source', Text, nullable=True)
    read_only = Column('read_only', Text, nullable=True)
    access_key_id = Column('access_key_id', Text, nullable=True)
    resource_name = Column('resource_name', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)