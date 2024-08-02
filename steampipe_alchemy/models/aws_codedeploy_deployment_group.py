from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodedeployDeploymentGroup(Base, FormatMixins):
    __tablename__ = 'aws_codedeploy_deployment_group'
    _ctx = Column('_ctx', JSON, nullable=True)
    last_successful_deployment = Column('last_successful_deployment', JSON, nullable=True)
    load_balancer_info = Column('load_balancer_info', JSON, nullable=True)
    on_premises_instance_tag_filters = Column('on_premises_instance_tag_filters', JSON, nullable=True)
    on_premises_tag_set = Column('on_premises_tag_set', JSON, nullable=True)
    outdated_instances_strategy = Column('outdated_instances_strategy', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    target_revision = Column('target_revision', JSON, nullable=True)
    trigger_configurations = Column('trigger_configurations', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    alarm_configuration = Column('alarm_configuration', JSON, nullable=True)
    auto_rollback_configuration = Column('auto_rollback_configuration', JSON, nullable=True)
    auto_scaling_groups = Column('auto_scaling_groups', JSON, nullable=True)
    blue_green_deployment_configuration = Column('blue_green_deployment_configuration', JSON, nullable=True)
    compute_platform = Column('compute_platform', JSON, nullable=True)
    deployment_style = Column('deployment_style', JSON, nullable=True)
    ec2_tag_filters = Column('ec2_tag_filters', JSON, nullable=True)
    ec2_tag_set = Column('ec2_tag_set', JSON, nullable=True)
    ecs_services = Column('ecs_services', JSON, nullable=True)
    last_attempted_deployment = Column('last_attempted_deployment', JSON, nullable=True)
    application_name = Column('application_name', Text, nullable=True)
    deployment_config_name = Column('deployment_config_name', Text, nullable=True)
    deployment_group_id = Column('deployment_group_id', Text, nullable=True)
    deployment_group_name = Column('deployment_group_name', Text, nullable=True)
    service_role_arn = Column('service_role_arn', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)