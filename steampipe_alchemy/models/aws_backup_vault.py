from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsBackupVault(Base):
    __tablename__ = 'aws_backup_vault'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    creator_request_id = Column('creator_request_id', Text, nullable=True)
    encryption_key_arn = Column('encryption_key_arn', Text, nullable=True)
    number_of_recovery_points = Column('number_of_recovery_points', psql.DOUBLE_PRECISION, nullable=True)
    sns_topic_arn = Column('sns_topic_arn', Text, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    backup_vault_events = Column('backup_vault_events', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)