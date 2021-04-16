from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSnsTopicSubscription(Base):
    __tablename__ = 'aws_sns_topic_subscription'
    subscription_arn = Column(Text, name='subscription_arn', nullable=True)
    topic_arn = Column(Text, name='topic_arn', nullable=True)
    owner = Column(Text, name='owner', nullable=True)
    protocol = Column(Text, name='protocol', nullable=True)
    endpoint = Column(Text, name='endpoint', nullable=True)
    confirmation_was_authenticated = Column(Boolean, name='confirmation_was_authenticated', nullable=True)
    pending_confirmation = Column(Boolean, name='pending_confirmation', nullable=True)
    raw_message_delivery = Column(Boolean, name='raw_message_delivery', nullable=True)
    delivery_policy = Column(JSON, name='delivery_policy', nullable=True)
    effective_delivery_policy = Column(JSON, name='effective_delivery_policy', nullable=True)
    redrive_policy = Column(JSON, name='redrive_policy', nullable=True)
    filter_policy = Column(JSON, name='filter_policy', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)