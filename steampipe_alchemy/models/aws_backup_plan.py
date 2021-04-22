from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsBackupPlan(Base):
    __tablename__ = 'aws_backup_plan'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    backup_plan_id = Column('backup_plan_id', Text, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    deletion_date = Column('deletion_date', TIMESTAMP, nullable=True)
    last_execution_date = Column('last_execution_date', TIMESTAMP, nullable=True)
    creator_request_id = Column('creator_request_id', Text, nullable=True)
    version_id = Column('version_id', Text, nullable=True)
    backup_plan = Column('backup_plan', JSON, nullable=True)
    advanced_backup_settings = Column('advanced_backup_settings', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)