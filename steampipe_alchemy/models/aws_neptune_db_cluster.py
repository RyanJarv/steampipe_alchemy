from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsNeptuneDbCluster(Base, FormatMixins):
    __tablename__ = 'aws_neptune_db_cluster'
    cluster_create_time = Column('cluster_create_time', TIMESTAMP, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    deletion_protection = Column('deletion_protection', Boolean, nullable=True)
    earliest_restorable_time = Column('earliest_restorable_time', TIMESTAMP, nullable=True)
    copy_tags_to_snapshot = Column('copy_tags_to_snapshot', Boolean, nullable=True)
    storage_encrypted = Column('storage_encrypted', Boolean, nullable=True)
    associated_roles = Column('associated_roles', JSON, nullable=True)
    availability_zones = Column('availability_zones', JSON, nullable=True)
    db_cluster_members = Column('db_cluster_members', JSON, nullable=True)
    enabled_cloudwatch_logs_exports = Column('enabled_cloudwatch_logs_exports', JSON, nullable=True)
    read_replica_identifiers = Column('read_replica_identifiers', JSON, nullable=True)
    vpc_security_groups = Column('vpc_security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    cross_account_clone = Column('cross_account_clone', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    allocated_storage = Column('allocated_storage', BigInteger, nullable=True)
    automatic_restart_time = Column('automatic_restart_time', TIMESTAMP, nullable=True)
    iam_database_authentication_enabled = Column('iam_database_authentication_enabled', Boolean, nullable=True)
    backup_retention_period = Column('backup_retention_period', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    latest_restorable_time = Column('latest_restorable_time', TIMESTAMP, nullable=True)
    multi_az = Column('multi_az', Boolean, nullable=True)
    reader_endpoint = Column('reader_endpoint', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    clone_group_id = Column('clone_group_id', Text, nullable=True)
    db_cluster_parameter_group = Column('db_cluster_parameter_group', Text, nullable=True)
    db_subnet_group = Column('db_subnet_group', Text, nullable=True)
    database_name = Column('database_name', Text, nullable=True)
    db_cluster_resource_id = Column('db_cluster_resource_id', Text, nullable=True)
    endpoint = Column('endpoint', Text, nullable=True)
    engine = Column('engine', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    hosted_zone_id = Column('hosted_zone_id', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    percent_progress = Column('percent_progress', Text, nullable=True)
    preferred_backup_window = Column('preferred_backup_window', Text, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    db_cluster_identifier = Column('db_cluster_identifier', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)