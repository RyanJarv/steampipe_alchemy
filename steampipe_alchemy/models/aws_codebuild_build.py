from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodebuildBuild(Base, FormatMixins):
    __tablename__ = 'aws_codebuild_build'
    _ctx = Column('_ctx', JSON, nullable=True)
    environment = Column('environment', JSON, nullable=True)
    exported_environment_variables = Column('exported_environment_variables', JSON, nullable=True)
    file_system_locations = Column('file_system_locations', JSON, nullable=True)
    logs = Column('logs', JSON, nullable=True)
    network_interfaces = Column('network_interfaces', JSON, nullable=True)
    phases = Column('phases', JSON, nullable=True)
    report_arns = Column('report_arns', JSON, nullable=True)
    secondary_artifacts = Column('secondary_artifacts', JSON, nullable=True)
    secondary_source_versions = Column('secondary_source_versions', JSON, nullable=True)
    secondary_sources = Column('secondary_sources', JSON, nullable=True)
    source = Column('source', JSON, nullable=True)
    vpc_config = Column('vpc_config', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    build_complete = Column('build_complete', Boolean, nullable=True)
    build_number = Column('build_number', BigInteger, nullable=True)
    build_status = Column('build_status', JSON, nullable=True)
    end_time = Column('end_time', TIMESTAMP, nullable=True)
    queued_timeout_in_minutes = Column('queued_timeout_in_minutes', BigInteger, nullable=True)
    start_time = Column('start_time', TIMESTAMP, nullable=True)
    timeout_in_minutes = Column('timeout_in_minutes', BigInteger, nullable=True)
    artifacts = Column('artifacts', JSON, nullable=True)
    cache = Column('cache', JSON, nullable=True)
    debug_session = Column('debug_session', JSON, nullable=True)
    id = Column('id', Text, nullable=True)
    build_batch_arn = Column('build_batch_arn', Text, nullable=True)
    resolved_source_version = Column('resolved_source_version', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    current_phase = Column('current_phase', Text, nullable=True)
    encryption_key = Column('encryption_key', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    initiator = Column('initiator', Text, nullable=True)
    project_name = Column('project_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    source_version = Column('source_version', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)