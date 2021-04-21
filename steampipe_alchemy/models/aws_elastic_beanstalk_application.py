from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticBeanstalkApplication(Base):
    __tablename__ = 'aws_elastic_beanstalk_application'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    date_created = Column(name='date_created', type_=TIMESTAMP, nullable=True)
    date_updated = Column(name='date_updated', type_=TIMESTAMP, nullable=True)
    configuration_templates = Column(name='configuration_templates', type_=JSON, nullable=True)
    versions = Column(name='versions', type_=JSON, nullable=True)
    resource_lifecycle_config = Column(name='resource_lifecycle_config', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)