from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsElasticBeanstalkApplicationVersion(Base, FormatMixins):
    __tablename__ = 'aws_elastic_beanstalk_application_version'
    _ctx = Column('_ctx', JSON, nullable=True)
    date_created = Column('date_created', TIMESTAMP, nullable=True)
    date_updated = Column('date_updated', TIMESTAMP, nullable=True)
    source_build_information = Column('source_build_information', JSON, nullable=True)
    source_bundle = Column('source_bundle', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    application_version_arn = Column('application_version_arn', Text, nullable=True)
    build_arn = Column('build_arn', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    application_name = Column('application_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    version_label = Column('version_label', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)