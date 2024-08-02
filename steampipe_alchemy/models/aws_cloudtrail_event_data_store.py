from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudtrailEventDataStore(Base, FormatMixins):
    __tablename__ = 'aws_cloudtrail_event_data_store'
    _ctx = Column('_ctx', JSON, nullable=True)
    multi_region_enabled = Column('multi_region_enabled', Boolean, nullable=True)
    organization_enabled = Column('organization_enabled', Boolean, nullable=True)
    retention_period = Column('retention_period', BigInteger, nullable=True)
    termination_protection_enabled = Column('termination_protection_enabled', Boolean, nullable=True)
    updated_timestamp = Column('updated_timestamp', TIMESTAMP, nullable=True)
    advanced_event_selectors = Column('advanced_event_selectors', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    created_timestamp = Column('created_timestamp', TIMESTAMP, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)