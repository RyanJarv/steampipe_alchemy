from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEcsService(Base, FormatMixins):
    __tablename__ = 'aws_ecs_service'
    deployment_configuration = Column('deployment_configuration', JSON, nullable=True)
    deployments = Column('deployments', JSON, nullable=True)
    events = Column('events', JSON, nullable=True)
    load_balancers = Column('load_balancers', JSON, nullable=True)
    network_configuration = Column('network_configuration', JSON, nullable=True)
    placement_constraints = Column('placement_constraints', JSON, nullable=True)
    placement_strategy = Column('placement_strategy', JSON, nullable=True)
    service_registries = Column('service_registries', JSON, nullable=True)
    task_sets = Column('task_sets', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    pending_count = Column('pending_count', BigInteger, nullable=True)
    desired_count = Column('desired_count', BigInteger, nullable=True)
    enable_ecs_managed_tags = Column('enable_ecs_managed_tags', Boolean, nullable=True)
    enable_execute_command = Column('enable_execute_command', Boolean, nullable=True)
    running_count = Column('running_count', BigInteger, nullable=True)
    health_check_grace_period_seconds = Column('health_check_grace_period_seconds', BigInteger, nullable=True)
    capacity_provider_strategy = Column('capacity_provider_strategy', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    cluster_arn = Column('cluster_arn', Text, nullable=True)
    task_definition = Column('task_definition', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    deployment_controller_type = Column('deployment_controller_type', Text, nullable=True)
    launch_type = Column('launch_type', Text, nullable=True)
    platform_version = Column('platform_version', Text, nullable=True)
    propagate_tags = Column('propagate_tags', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    scheduling_strategy = Column('scheduling_strategy', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    service_name = Column('service_name', Text, nullable=True)