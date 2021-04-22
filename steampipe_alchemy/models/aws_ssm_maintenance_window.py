from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSsmMaintenanceWindow(Base):
    __tablename__ = 'aws_ssm_maintenance_window'
    name = Column('name', Text, primary_key=True, nullable=True)
    window_id = Column('window_id', Text, nullable=True)
    enabled = Column('enabled', Boolean, nullable=True)
    allow_unassociated_targets = Column('allow_unassociated_targets', Boolean, nullable=True)
    description = Column('description', Text, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    duration = Column('duration', BigInteger, nullable=True)
    cutoff = Column('cutoff', BigInteger, nullable=True)
    schedule = Column('schedule', Text, nullable=True)
    schedule_offset = Column('schedule_offset', BigInteger, nullable=True)
    targets = Column('targets', JSON, nullable=True)
    tasks = Column('tasks', JSON, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    end_date = Column('end_date', Text, nullable=True)
    schedule_timezone = Column('schedule_timezone', Text, nullable=True)
    start_date = Column('start_date', Text, nullable=True)
    modified_date = Column('modified_date', TIMESTAMP, nullable=True)
    next_execution_time = Column('next_execution_time', TIMESTAMP, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)