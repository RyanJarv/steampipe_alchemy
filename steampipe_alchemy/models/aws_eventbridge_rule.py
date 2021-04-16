from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEventbridgeRule(Base):
    __tablename__ = 'aws_eventbridge_rule'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    description = Column(Text, name='description', nullable=True)
    state = Column(Text, name='state', nullable=True)
    event_bus_name = Column(Text, name='event_bus_name', nullable=True)
    created_by = Column(Text, name='created_by', nullable=True)
    managed_by = Column(Text, name='managed_by', nullable=True)
    event_pattern = Column(JSON, name='event_pattern', nullable=True)
    targets = Column(JSON, name='targets', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)