from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsElasticBeanstalkEnvironment(Base, FormatMixins):
    __tablename__ = 'aws_elastic_beanstalk_environment'
    environment_name = Column('environment_name', Text, nullable=True)
    environment_id = Column('environment_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    date_created = Column('date-created', TIMESTAMP, nullable=True)
    abortable_operation_in_progress = Column('abortable_operation_in_progress', Boolean, nullable=True)
    application_name = Column('application_name', Text, nullable=True)
    cname = Column('cname', Text, nullable=True)
    date_updated = Column('date_updated', TIMESTAMP, nullable=True)
    endpoint_url = Column('endpoint_url', Text, nullable=True)
    health = Column('health', Text, nullable=True)
    health_status = Column('health_status', Text, nullable=True)
    operations_role = Column('operations_role', Text, nullable=True)
    platform_arn = Column('platform_arn', Text, nullable=True)
    solution_stack_name = Column('solution_stack_name', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    template_name = Column('template_name', Text, nullable=True)
    version_label = Column('version_label', Text, nullable=True)
    environment_links = Column('environment_links', JSON, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    tier = Column('tier', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsElasticBeanstalkEnvironmentLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_elastic_beanstalk_environment_local'
    environment_name = Column('environment_name', Text, nullable=True)
    environment_id = Column('environment_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    date_created = Column('date-created', TIMESTAMP, nullable=True)
    abortable_operation_in_progress = Column('abortable_operation_in_progress', Boolean, nullable=True)
    application_name = Column('application_name', Text, nullable=True)
    cname = Column('cname', Text, nullable=True)
    date_updated = Column('date_updated', TIMESTAMP, nullable=True)
    endpoint_url = Column('endpoint_url', Text, nullable=True)
    health = Column('health', Text, nullable=True)
    health_status = Column('health_status', Text, nullable=True)
    operations_role = Column('operations_role', Text, nullable=True)
    platform_arn = Column('platform_arn', Text, nullable=True)
    solution_stack_name = Column('solution_stack_name', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    template_name = Column('template_name', Text, nullable=True)
    version_label = Column('version_label', Text, nullable=True)
    environment_links = Column('environment_links', JSON, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    tier = Column('tier', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsElasticBeanstalkEnvironment).select_from(AwsElasticBeanstalkEnvironment)
create_materialized_view('aws_elastic_beanstalk_environment_local', cache, db.metadata_materialized)
