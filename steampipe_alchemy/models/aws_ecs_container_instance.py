from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEcsContainerInstance(Base, FormatMixins):
    __tablename__ = 'aws_ecs_container_instance'
    attributes = Column('attributes', JSON, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    version_info = Column('version_info', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    agent_connected = Column('agent_connected', Boolean, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    pending_tasks_count = Column('pending_tasks_count', BigInteger, nullable=True)
    registered_at = Column('registered_at', TIMESTAMP, nullable=True)
    registered_resources = Column('registered_resources', JSON, nullable=True)
    remaining_resources = Column('remaining_resources', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    running_tasks_count = Column('running_tasks_count', BigInteger, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    status = Column('status', Text, nullable=True)
    ec2_instance_id = Column('ec2_instance_id', Text, nullable=True)
    cluster_arn = Column('cluster_arn', Text, nullable=True)
    agent_update_status = Column('agent_update_status', Text, nullable=True)
    capacity_provider_name = Column('capacity_provider_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status_reason = Column('status_reason', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)