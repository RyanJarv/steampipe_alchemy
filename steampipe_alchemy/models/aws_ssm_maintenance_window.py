from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSsmMaintenanceWindow(Base):
    __tablename__ = 'aws_ssm_maintenance_window'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    window_id = Column(Text, name='window_id', nullable=True)
    enabled = Column(Boolean, name='enabled', nullable=True)
    allow_unassociated_targets = Column(Boolean, name='allow_unassociated_targets', nullable=True)
    description = Column(Text, name='description', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    duration = Column(BigInteger, name='duration', nullable=True)
    cutoff = Column(BigInteger, name='cutoff', nullable=True)
    schedule = Column(Text, name='schedule', nullable=True)
    schedule_offset = Column(BigInteger, name='schedule_offset', nullable=True)
    targets = Column(JSON, name='targets', nullable=True)
    tasks = Column(JSON, name='tasks', nullable=True)
    created_date = Column(TIMESTAMP, name='created_date', nullable=True)
    end_date = Column(Text, name='end_date', nullable=True)
    schedule_timezone = Column(Text, name='schedule_timezone', nullable=True)
    start_date = Column(Text, name='start_date', nullable=True)
    modified_date = Column(TIMESTAMP, name='modified_date', nullable=True)
    next_execution_time = Column(TIMESTAMP, name='next_execution_time', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)