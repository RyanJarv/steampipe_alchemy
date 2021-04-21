from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSsmMaintenanceWindow(Base):
    __tablename__ = 'aws_ssm_maintenance_window'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    window_id = Column(name='window_id', type_=Text, nullable=True)
    enabled = Column(name='enabled', type_=Boolean, nullable=True)
    allow_unassociated_targets = Column(name='allow_unassociated_targets', type_=Boolean, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    duration = Column(name='duration', type_=BigInteger, nullable=True)
    cutoff = Column(name='cutoff', type_=BigInteger, nullable=True)
    schedule = Column(name='schedule', type_=Text, nullable=True)
    schedule_offset = Column(name='schedule_offset', type_=BigInteger, nullable=True)
    targets = Column(name='targets', type_=JSON, nullable=True)
    tasks = Column(name='tasks', type_=JSON, nullable=True)
    created_date = Column(name='created_date', type_=TIMESTAMP, nullable=True)
    end_date = Column(name='end_date', type_=Text, nullable=True)
    schedule_timezone = Column(name='schedule_timezone', type_=Text, nullable=True)
    start_date = Column(name='start_date', type_=Text, nullable=True)
    modified_date = Column(name='modified_date', type_=TIMESTAMP, nullable=True)
    next_execution_time = Column(name='next_execution_time', type_=TIMESTAMP, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)