from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsBackupJob(Base, FormatMixins):
    __tablename__ = 'aws_backup_job'
    _ctx = Column('_ctx', JSON, nullable=True)
    backup_size = Column('backup_size', BigInteger, nullable=True)
    backup_options = Column('backup_options', JSON, nullable=True)
    bytes_transferred = Column('bytes_transferred', BigInteger, nullable=True)
    completion_date = Column('completion_date', TIMESTAMP, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    expected_completion_date = Column('expected_completion_date', TIMESTAMP, nullable=True)
    is_parent = Column('is_parent', Boolean, nullable=True)
    start_by = Column('start_by', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    backup_type = Column('backup_type', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    iam_role_arn = Column('iam_role_arn', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    parent_job_id = Column('parent_job_id', Text, nullable=True)
    recovery_point_arn = Column('recovery_point_arn', Text, nullable=True)
    backup_vault_arn = Column('backup_vault_arn', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    resource_arn = Column('resource_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    percent_done = Column('percent_done', Text, nullable=True)
    backup_vault_name = Column('backup_vault_name', Text, nullable=True)
    job_id = Column('job_id', Text, nullable=True)