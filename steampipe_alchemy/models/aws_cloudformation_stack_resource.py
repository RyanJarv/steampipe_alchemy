from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudformationStackResource(Base, FormatMixins):
    __tablename__ = 'aws_cloudformation_stack_resource'
    _ctx = Column('_ctx', JSON, nullable=True)
    last_updated_timestamp = Column('last_updated_timestamp', TIMESTAMP, nullable=True)
    drift_information = Column('drift_information', JSON, nullable=True)
    module_info = Column('module_info', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    physical_resource_id = Column('physical_resource_id', Text, nullable=True)
    resource_status_reason = Column('resource_status_reason', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    logical_resource_id = Column('logical_resource_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    stack_name = Column('stack_name', Text, nullable=True)
    stack_id = Column('stack_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    resource_status = Column('resource_status', Text, nullable=True)