from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsmManagedInstance(Base, FormatMixins):
    __tablename__ = 'aws_ssm_managed_instance'
    _ctx = Column('_ctx', JSON, nullable=True)
    ip_address = Column('ip_address', psql.INET, nullable=True)
    is_latest_version = Column('is_latest_version', Boolean, nullable=True)
    last_association_execution_date = Column('last_association_execution_date', TIMESTAMP, nullable=True)
    last_ping_date_time = Column('last_ping_date_time', TIMESTAMP, nullable=True)
    last_successful_association_execution_date = Column('last_successful_association_execution_date', TIMESTAMP, nullable=True)
    registration_date = Column('registration_date', TIMESTAMP, nullable=True)
    association_overview = Column('association_overview', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    platform_name = Column('platform_name', Text, nullable=True)
    platform_type = Column('platform_type', Text, nullable=True)
    platform_version = Column('platform_version', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    instance_id = Column('instance_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    ping_status = Column('ping_status', Text, nullable=True)
    activation_id = Column('activation_id', Text, nullable=True)
    agent_version = Column('agent_version', Text, nullable=True)
    association_status = Column('association_status', Text, nullable=True)
    computer_name = Column('computer_name', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)