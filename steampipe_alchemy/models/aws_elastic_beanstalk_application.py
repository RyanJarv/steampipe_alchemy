from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsElasticBeanstalkApplication(Base):
    __tablename__ = 'aws_elastic_beanstalk_application'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    description = Column(Text, name='description', nullable=True)
    date_created = Column(TIMESTAMP, name='date_created', nullable=True)
    date_updated = Column(TIMESTAMP, name='date_updated', nullable=True)
    configuration_templates = Column(JSON, name='configuration_templates', nullable=True)
    versions = Column(JSON, name='versions', nullable=True)
    resource_lifecycle_config = Column(JSON, name='resource_lifecycle_config', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)