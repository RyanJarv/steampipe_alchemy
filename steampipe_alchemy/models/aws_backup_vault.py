from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsBackupVault(Base):
    __tablename__ = 'aws_backup_vault'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    creation_date = Column(TIMESTAMP, name='creation_date', nullable=True)
    creator_request_id = Column(Text, name='creator_request_id', nullable=True)
    encryption_key_arn = Column(Text, name='encryption_key_arn', nullable=True)
    number_of_recovery_points = Column(psql.DOUBLE_PRECISION, name='number_of_recovery_points', nullable=True)
    sns_topic_arn = Column(Text, name='sns_topic_arn', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    backup_vault_events = Column(JSON, name='backup_vault_events', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)