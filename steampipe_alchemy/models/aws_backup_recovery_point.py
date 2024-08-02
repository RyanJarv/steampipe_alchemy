from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsBackupRecoveryPoint(Base, FormatMixins):
    __tablename__ = 'aws_backup_recovery_point'
    is_encrypted = Column('is_encrypted', Boolean, nullable=True)
    calculated_lifecycle = Column('calculated_lifecycle', JSON, nullable=True)
    created_by = Column('created_by', JSON, nullable=True)
    lifecycle = Column('lifecycle', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    last_restore_time = Column('last_restore_time', TIMESTAMP, nullable=True)
    completion_date = Column('completion_date', TIMESTAMP, nullable=True)
    backup_size_in_bytes = Column('backup_size_in_bytes', BigInteger, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    source_backup_vault_arn = Column('source_backup_vault_arn', Text, nullable=True)
    recovery_point_arn = Column('recovery_point_arn', Text, primary_key=True, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    backup_vault_arn = Column('backup_vault_arn', Text, nullable=True)
    encryption_key_arn = Column('encryption_key_arn', Text, nullable=True)
    iam_role_arn = Column('iam_role_arn', Text, nullable=True)
    resource_arn = Column('resource_arn', Text, nullable=True)
    backup_vault_name = Column('backup_vault_name', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    storage_class = Column('storage_class', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)