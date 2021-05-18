from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsElasticBeanstalkApplication(Base, FormatMixins):
    __tablename__ = 'aws_elastic_beanstalk_application'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    date_created = Column('date_created', TIMESTAMP, nullable=True)
    date_updated = Column('date_updated', TIMESTAMP, nullable=True)
    configuration_templates = Column('configuration_templates', JSON, nullable=True)
    versions = Column('versions', JSON, nullable=True)
    resource_lifecycle_config = Column('resource_lifecycle_config', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsElasticBeanstalkApplicationLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_elastic_beanstalk_application_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    date_created = Column('date_created', TIMESTAMP, nullable=True)
    date_updated = Column('date_updated', TIMESTAMP, nullable=True)
    configuration_templates = Column('configuration_templates', JSON, nullable=True)
    versions = Column('versions', JSON, nullable=True)
    resource_lifecycle_config = Column('resource_lifecycle_config', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsElasticBeanstalkApplication).select_from(AwsElasticBeanstalkApplication)
create_materialized_view('aws_elastic_beanstalk_application_local', cache, db.metadata_materialized)
