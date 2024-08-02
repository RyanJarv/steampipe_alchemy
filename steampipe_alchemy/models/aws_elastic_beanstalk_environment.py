from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsElasticBeanstalkEnvironment(Base, FormatMixins):
    __tablename__ = 'aws_elastic_beanstalk_environment'
    managed_actions = Column('managed_actions', JSON, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    tier = Column('tier', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    date_created = Column('date_created', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    abortable_operation_in_progress = Column('abortable_operation_in_progress', Boolean, nullable=True)
    date_updated = Column('date_updated', TIMESTAMP, nullable=True)
    configuration_settings = Column('configuration_settings', JSON, nullable=True)
    environment_links = Column('environment_links', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    environment_name = Column('environment_name', Text, nullable=True)
    version_label = Column('version_label', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    template_name = Column('template_name', Text, nullable=True)
    environment_id = Column('environment_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    application_name = Column('application_name', Text, nullable=True)
    cname = Column('cname', Text, nullable=True)
    endpoint_url = Column('endpoint_url', Text, nullable=True)
    health = Column('health', Text, nullable=True)
    health_status = Column('health_status', Text, nullable=True)
    operations_role = Column('operations_role', Text, nullable=True)
    platform_arn = Column('platform_arn', Text, nullable=True)
    solution_stack_name = Column('solution_stack_name', Text, nullable=True)
    status = Column('status', Text, nullable=True)