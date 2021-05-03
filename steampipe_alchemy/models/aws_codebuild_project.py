from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodebuildProject(Base, FormatMixins):
    __tablename__ = 'aws_codebuild_project'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    concurrent_build_limit = Column('concurrent_build_limit', BigInteger, nullable=True)
    created = Column('created', TIMESTAMP, nullable=True)
    last_modified = Column('last_modified', TIMESTAMP, nullable=True)
    encryption_key = Column('encryption_key', Text, nullable=True)
    queued_timeout_in_minutes = Column('queued_timeout_in_minutes', BigInteger, nullable=True)
    service_role = Column('service_role', Text, nullable=True)
    source_version = Column('source_version', Text, nullable=True)
    timeout_in_minutes = Column('timeout_in_minutes', BigInteger, nullable=True)
    artifacts = Column('artifacts', JSON, nullable=True)
    badge = Column('badge', JSON, nullable=True)
    build_batch_config = Column('build_batch_config', JSON, nullable=True)
    cache = Column('cache', JSON, nullable=True)
    environment = Column('environment', JSON, nullable=True)
    file_system_locations = Column('file_system_locations', JSON, nullable=True)
    logs_config = Column('logs_config', JSON, nullable=True)
    secondary_artifacts = Column('secondary_artifacts', JSON, nullable=True)
    secondary_source_versions = Column('secondary_source_versions', JSON, nullable=True)
    secondary_sources = Column('secondary_sources', JSON, nullable=True)
    source = Column('source', JSON, nullable=True)
    vpc_config = Column('vpc_config', JSON, nullable=True)
    webhook = Column('webhook', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)