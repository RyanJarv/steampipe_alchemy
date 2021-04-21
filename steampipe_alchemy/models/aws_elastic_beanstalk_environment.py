from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticBeanstalkEnvironment(Base):
    __tablename__ = 'aws_elastic_beanstalk_environment'
    environment_name = Column(name='environment_name', type_=Text, nullable=True)
    environment_id = Column(name='environment_id', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    date_created = Column(name='date-created', type_=TIMESTAMP, nullable=True)
    abortable_operation_in_progress = Column(name='abortable_operation_in_progress', type_=Boolean, nullable=True)
    application_name = Column(name='application_name', type_=Text, nullable=True)
    cname = Column(name='cname', type_=Text, nullable=True)
    date_updated = Column(name='date_updated', type_=TIMESTAMP, nullable=True)
    endpoint_url = Column(name='endpoint_url', type_=Text, nullable=True)
    health = Column(name='health', type_=Text, nullable=True)
    health_status = Column(name='health_status', type_=Text, nullable=True)
    operations_role = Column(name='operations_role', type_=Text, nullable=True)
    platform_arn = Column(name='platform_arn', type_=Text, nullable=True)
    solution_stack_name = Column(name='solution_stack_name', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    template_name = Column(name='template_name', type_=Text, nullable=True)
    version_label = Column(name='version_label', type_=Text, nullable=True)
    environment_links = Column(name='environment_links', type_=JSON, nullable=True)
    resources = Column(name='resources', type_=JSON, nullable=True)
    tier = Column(name='tier', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)