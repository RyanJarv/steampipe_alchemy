from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsKinesisanalyticsv2Application(Base, FormatMixins):
    __tablename__ = 'aws_kinesisanalyticsv2_application'
    cloud_watch_logging_option_descriptions = Column('cloud_watch_logging_option_descriptions', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    last_update_timestamp = Column('last_update_timestamp', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    create_timestamp = Column('create_timestamp', TIMESTAMP, nullable=True)
    application_version_id = Column('application_version_id', BigInteger, nullable=True)
    application_configuration_description = Column('application_configuration_description', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    application_name = Column('application_name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    application_arn = Column('application_arn', Text, nullable=True)
    application_status = Column('application_status', Text, nullable=True)
    application_description = Column('application_description', Text, nullable=True)
    runtime_environment = Column('runtime_environment', Text, nullable=True)
    service_execution_role = Column('service_execution_role', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)