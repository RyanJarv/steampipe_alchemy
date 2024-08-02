from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRdsDbInstanceAutomatedBackup(Base, FormatMixins):
    __tablename__ = 'aws_rds_db_instance_automated_backup'
    iops = Column('iops', BigInteger, nullable=True)
    encrypted = Column('encrypted', Boolean, nullable=True)
    allocated_storage = Column('allocated_storage', BigInteger, nullable=True)
    db_instance_automated_backups_replications = Column('db_instance_automated_backups_replications', JSON, nullable=True)
    restore_window = Column('restore_window', JSON, nullable=True)
    backup_retention_period = Column('backup_retention_period', BigInteger, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    iam_database_authentication_enabled = Column('iam_database_authentication_enabled', Boolean, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    storage_throughput = Column('storage_throughput', BigInteger, nullable=True)
    instance_create_time = Column('instance_create_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    storage_type = Column('storage_type', Text, nullable=True)
    tde_credential_arn = Column('tde_credential_arn', Text, nullable=True)
    timezone = Column('timezone', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    master_username = Column('master_username', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    db_instance_arn = Column('db_instance_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    backup_target = Column('backup_target', Text, nullable=True)
    dbi_resource_id = Column('dbi_resource_id', Text, nullable=True)
    engine = Column('engine', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    license_model = Column('license_model', Text, nullable=True)
    db_instance_identifier = Column('db_instance_identifier', Text, nullable=True)
    option_group_name = Column('option_group_name', Text, nullable=True)