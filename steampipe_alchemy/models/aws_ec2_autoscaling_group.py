from steampipe_alchemy.types.aws_ec2_autoscaling_group import *

from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2AutoscalingGroup(Base):
    __tablename__ = 'aws_ec2_autoscaling_group'
    name = Column('name', Text, primary_key=True, nullable=True)
    autoscaling_group_arn = Column('autoscaling_group_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    new_instances_protected_from_scale_in = Column('new_instances_protected_from_scale_in', Boolean, nullable=True)
    launch_configuration_name = Column('launch_configuration_name', Text, nullable=True)
    default_cooldown = Column('default_cooldown', BigInteger, nullable=True)
    desired_capacity = Column('desired_capacity', BigInteger, nullable=True)
    max_instance_lifetime = Column('max_instance_lifetime', BigInteger, nullable=True)
    max_size = Column('max_size', BigInteger, nullable=True)
    min_size = Column('min_size', BigInteger, nullable=True)
    health_check_grace_period = Column('health_check_grace_period', BigInteger, nullable=True)
    health_check_type = Column('health_check_type', Text, nullable=True)
    placement_group = Column('placement_group', Text, nullable=True)
    service_linked_role_arn = Column('service_linked_role_arn', Text, nullable=True)
    vpc_zone_identifier = Column('vpc_zone_identifier', Text, nullable=True)
    launch_template_name = Column('launch_template_name', Text, nullable=True)
    launch_template_id = Column('launch_template_id', Text, nullable=True)
    launch_template_version = Column('launch_template_version', Text, nullable=True)
    on_demand_allocation_strategy = Column('on_demand_allocation_strategy', Text, nullable=True)
    on_demand_base_capacity = Column('on_demand_base_capacity', BigInteger, nullable=True)
    on_demand_percentage_above_base_capacity = Column('on_demand_percentage_above_base_capacity', BigInteger, nullable=True)
    spot_allocation_strategy = Column('spot_allocation_strategy', Text, nullable=True)
    spot_instance_pools = Column('spot_instance_pools', BigInteger, nullable=True)
    spot_max_price = Column('spot_max_price', Text, nullable=True)
    mixed_instances_policy_launch_template_name = Column('mixed_instances_policy_launch_template_name', Text, nullable=True)
    mixed_instances_policy_launch_template_id = Column('mixed_instances_policy_launch_template_id', Text, nullable=True)
    mixed_instances_policy_launch_template_version = Column('mixed_instances_policy_launch_template_version', Text, nullable=True)
    mixed_instances_policy_launch_template_overrides = Column('mixed_instances_policy_launch_template_overrides', JSON, nullable=True)
    availability_zones = Column('availability_zones', JSON, nullable=True)
    load_balancer_names = Column('load_balancer_names', JSON, nullable=True)
    target_group_arns = Column('target_group_arns', JSON, nullable=True)
    instances = Column('instances', JSON, nullable=True)
    enabled_metrics = Column('enabled_metrics', JSON, nullable=True)
    policies = Column('policies', JSON, nullable=True)
    termination_policies = Column('termination_policies', JSON, nullable=True)
    suspended_processes = Column('suspended_processes', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)