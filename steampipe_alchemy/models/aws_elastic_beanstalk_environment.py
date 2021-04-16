from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsElasticBeanstalkEnvironment(Base):
    __tablename__ = 'aws_elastic_beanstalk_environment'
    environment_name = Column(Text, name='environment_name', nullable=True)
    environment_id = Column(Text, name='environment_id', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    description = Column(Text, name='description', nullable=True)
    date_created = Column(TIMESTAMP, name='date-created', nullable=True)
    abortable_operation_in_progress = Column(Boolean, name='abortable_operation_in_progress', nullable=True)
    application_name = Column(Text, name='application_name', nullable=True)
    cname = Column(Text, name='cname', nullable=True)
    date_updated = Column(TIMESTAMP, name='date_updated', nullable=True)
    endpoint_url = Column(Text, name='endpoint_url', nullable=True)
    health = Column(Text, name='health', nullable=True)
    health_status = Column(Text, name='health_status', nullable=True)
    operations_role = Column(Text, name='operations_role', nullable=True)
    platform_arn = Column(Text, name='platform_arn', nullable=True)
    solution_stack_name = Column(Text, name='solution_stack_name', nullable=True)
    status = Column(Text, name='status', nullable=True)
    template_name = Column(Text, name='template_name', nullable=True)
    version_label = Column(Text, name='version_label', nullable=True)
    environment_links = Column(JSON, name='environment_links', nullable=True)
    resources = Column(JSON, name='resources', nullable=True)
    tier = Column(JSON, name='tier', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)