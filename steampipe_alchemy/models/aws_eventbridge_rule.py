from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsEventbridgeRule(Base, FormatMixins):
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


# Local materialized view table
class AwsEventbridgeRuleLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_eventbridge_rule_local'
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


cache = select(AwsEventbridgeRule).select_from(AwsEventbridgeRule)
create_materialized_view('aws_eventbridge_rule_local', cache, db.metadata_materialized)
