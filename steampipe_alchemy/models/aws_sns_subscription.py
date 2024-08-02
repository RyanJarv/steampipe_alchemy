from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSnsSubscription(Base, FormatMixins):
    __tablename__ = 'aws_sns_subscription'
    _ctx = Column('_ctx', JSON, nullable=True)
    confirmation_was_authenticated = Column('confirmation_was_authenticated', Boolean, nullable=True)
    pending_confirmation = Column('pending_confirmation', Boolean, nullable=True)
    raw_message_delivery = Column('raw_message_delivery', Boolean, nullable=True)
    delivery_policy = Column('delivery_policy', JSON, nullable=True)
    effective_delivery_policy = Column('effective_delivery_policy', JSON, nullable=True)
    redrive_policy = Column('redrive_policy', JSON, nullable=True)
    filter_policy = Column('filter_policy', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    topic_arn = Column('topic_arn', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    protocol = Column('protocol', Text, nullable=True)
    endpoint = Column('endpoint', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    subscription_arn = Column('subscription_arn', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)