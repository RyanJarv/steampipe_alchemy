from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsElasticBeanstalkApplication(Base, FormatMixins):
    __tablename__ = 'aws_elastic_beanstalk_application'
    tags_src = Column('tags_src', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    date_created = Column('date_created', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    date_updated = Column('date_updated', TIMESTAMP, nullable=True)
    configuration_templates = Column('configuration_templates', JSON, nullable=True)
    versions = Column('versions', JSON, nullable=True)
    resource_lifecycle_config = Column('resource_lifecycle_config', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)