from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEventbridgeRule(Base):
    __tablename__ = 'aws_eventbridge_rule'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    event_bus_name = Column(name='event_bus_name', type_=Text, nullable=True)
    created_by = Column(name='created_by', type_=Text, nullable=True)
    managed_by = Column(name='managed_by', type_=Text, nullable=True)
    event_pattern = Column(name='event_pattern', type_=JSON, nullable=True)
    targets = Column(name='targets', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)