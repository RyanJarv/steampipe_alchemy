from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRdsDbEngineVersion(Base, FormatMixins):
    __tablename__ = 'aws_rds_db_engine_version'
    _ctx = Column('_ctx', JSON, nullable=True)
    list_supported_character_sets = Column('list_supported_character_sets', Boolean, nullable=True)
    list_supported_timezones = Column('list_supported_timezones', Boolean, nullable=True)
    default_only = Column('default_only', Boolean, nullable=True)
    supports_babelfish = Column('supports_babelfish', Boolean, nullable=True)
    supports_certificate_rotation_without_restart = Column('supports_certificate_rotation_without_restart', Boolean, nullable=True)
    supports_global_databases = Column('supports_global_databases', Boolean, nullable=True)
    supports_log_exports_to_cloudwatch_logs = Column('supports_log_exports_to_cloudwatch_logs', Boolean, nullable=True)
    supports_parallel_query = Column('supports_parallel_query', Boolean, nullable=True)
    supports_read_replica = Column('supports_read_replica', Boolean, nullable=True)
    exportable_log_types = Column('exportable_log_types', JSON, nullable=True)
    image = Column('image', JSON, nullable=True)
    supported_feature_names = Column('supported_feature_names', JSON, nullable=True)
    supported_nchar_character_sets = Column('supported_nchar_character_sets', JSON, nullable=True)
    supported_timezones = Column('supported_timezones', JSON, nullable=True)
    valid_upgrade_target = Column('valid_upgrade_target', JSON, nullable=True)
    tag_list = Column('tag_list', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    custom_db_engine_version_manifest = Column('custom_db_engine_version_manifest', Text, nullable=True)
    engine = Column('engine', Text, nullable=True)
    engine_mode = Column('engine_mode', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    db_engine_description = Column('db_engine_description', Text, nullable=True)
    db_engine_media_type = Column('db_engine_media_type', Text, nullable=True)
    db_engine_version_description = Column('db_engine_version_description', Text, nullable=True)
    db_parameter_group_family = Column('db_parameter_group_family', Text, nullable=True)
    database_installation_files_s3_bucket_name = Column('database_installation_files_s3_bucket_name', Text, nullable=True)
    database_installation_files_s3_prefix = Column('database_installation_files_s3_prefix', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    major_engine_version = Column('major_engine_version', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)