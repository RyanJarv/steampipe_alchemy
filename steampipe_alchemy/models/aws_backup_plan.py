from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsBackupPlan(Base):
    __tablename__ = 'aws_backup_plan'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    backup_plan_id = Column(name='backup_plan_id', type_=Text, nullable=True)
    creation_date = Column(name='creation_date', type_=TIMESTAMP, nullable=True)
    deletion_date = Column(name='deletion_date', type_=TIMESTAMP, nullable=True)
    last_execution_date = Column(name='last_execution_date', type_=TIMESTAMP, nullable=True)
    creator_request_id = Column(name='creator_request_id', type_=Text, nullable=True)
    version_id = Column(name='version_id', type_=Text, nullable=True)
    backup_plan = Column(name='backup_plan', type_=JSON, nullable=True)
    advanced_backup_settings = Column(name='advanced_backup_settings', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)