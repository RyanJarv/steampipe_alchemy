from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsBackupPlan(Base):
    __tablename__ = 'aws_backup_plan'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    backup_plan_id = Column(Text, name='backup_plan_id', nullable=True)
    creation_date = Column(TIMESTAMP, name='creation_date', nullable=True)
    deletion_date = Column(TIMESTAMP, name='deletion_date', nullable=True)
    last_execution_date = Column(TIMESTAMP, name='last_execution_date', nullable=True)
    creator_request_id = Column(Text, name='creator_request_id', nullable=True)
    version_id = Column(Text, name='version_id', nullable=True)
    backup_plan = Column(JSON, name='backup_plan', nullable=True)
    advanced_backup_settings = Column(JSON, name='advanced_backup_settings', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)