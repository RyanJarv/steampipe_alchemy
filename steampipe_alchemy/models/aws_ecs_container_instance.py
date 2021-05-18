from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsEcsContainerInstance(Base, FormatMixins):
    __tablename__ = 'aws_ecs_container_instance'
    arn = Column('arn', Text, primary_key=True, nullable=True)
    ec2_instance_id = Column('ec2_instance_id', Text, nullable=True)
    agent_connected = Column('agent_connected', Boolean, nullable=True)
    agent_update_status = Column('agent_update_status', Text, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    attributes = Column('attributes', JSON, nullable=True)
    capacity_provider_name = Column('capacity_provider_name', Text, nullable=True)
    pending_tasks_count = Column('pending_tasks_count', BigInteger, nullable=True)
    registered_at = Column('registered_at', TIMESTAMP, nullable=True)
    registered_resources = Column('registered_resources', JSON, nullable=True)
    remaining_resources = Column('remaining_resources', JSON, nullable=True)
    running_tasks_count = Column('running_tasks_count', BigInteger, nullable=True)
    status = Column('status', Text, nullable=True)
    status_reason = Column('status_reason', Text, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    version_info = Column('version_info', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsEcsContainerInstanceLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_ecs_container_instance_local'
    arn = Column('arn', Text, primary_key=True, nullable=True)
    ec2_instance_id = Column('ec2_instance_id', Text, nullable=True)
    agent_connected = Column('agent_connected', Boolean, nullable=True)
    agent_update_status = Column('agent_update_status', Text, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    attributes = Column('attributes', JSON, nullable=True)
    capacity_provider_name = Column('capacity_provider_name', Text, nullable=True)
    pending_tasks_count = Column('pending_tasks_count', BigInteger, nullable=True)
    registered_at = Column('registered_at', TIMESTAMP, nullable=True)
    registered_resources = Column('registered_resources', JSON, nullable=True)
    remaining_resources = Column('remaining_resources', JSON, nullable=True)
    running_tasks_count = Column('running_tasks_count', BigInteger, nullable=True)
    status = Column('status', Text, nullable=True)
    status_reason = Column('status_reason', Text, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    version_info = Column('version_info', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsEcsContainerInstance).select_from(AwsEcsContainerInstance)
create_materialized_view('aws_ecs_container_instance_local', cache, db.metadata_materialized)
