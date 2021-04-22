from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEventbridgeRule(Base):
    __tablename__ = 'aws_eventbridge_rule'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    event_bus_name = Column('event_bus_name', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    managed_by = Column('managed_by', Text, nullable=True)
    event_pattern = Column('event_pattern', JSON, nullable=True)
    targets = Column('targets', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)