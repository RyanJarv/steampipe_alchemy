from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsBackupLegalHold(Base, FormatMixins):
    __tablename__ = 'aws_backup_legal_hold'
    akas = Column('akas', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    retain_record_until = Column('retain_record_until', TIMESTAMP, nullable=True)
    recovery_point_selection = Column('recovery_point_selection', JSON, nullable=True)
    cancellation_date = Column('cancellation_date', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    legal_hold_id = Column('legal_hold_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)