from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsBackupVault(Base):
    __tablename__ = 'aws_backup_vault'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    creation_date = Column(name='creation_date', type_=TIMESTAMP, nullable=True)
    creator_request_id = Column(name='creator_request_id', type_=Text, nullable=True)
    encryption_key_arn = Column(name='encryption_key_arn', type_=Text, nullable=True)
    number_of_recovery_points = Column(name='number_of_recovery_points', type_=psql.DOUBLE_PRECISION, nullable=True)
    sns_topic_arn = Column(name='sns_topic_arn', type_=Text, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    backup_vault_events = Column(name='backup_vault_events', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)