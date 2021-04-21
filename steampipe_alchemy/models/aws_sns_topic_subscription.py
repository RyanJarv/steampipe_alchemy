from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSnsTopicSubscription(Base):
    __tablename__ = 'aws_sns_topic_subscription'
    subscription_arn = Column(name='subscription_arn', type_=Text, nullable=True)
    topic_arn = Column(name='topic_arn', type_=Text, nullable=True)
    owner = Column(name='owner', type_=Text, nullable=True)
    protocol = Column(name='protocol', type_=Text, nullable=True)
    endpoint = Column(name='endpoint', type_=Text, nullable=True)
    confirmation_was_authenticated = Column(name='confirmation_was_authenticated', type_=Boolean, nullable=True)
    pending_confirmation = Column(name='pending_confirmation', type_=Boolean, nullable=True)
    raw_message_delivery = Column(name='raw_message_delivery', type_=Boolean, nullable=True)
    delivery_policy = Column(name='delivery_policy', type_=JSON, nullable=True)
    effective_delivery_policy = Column(name='effective_delivery_policy', type_=JSON, nullable=True)
    redrive_policy = Column(name='redrive_policy', type_=JSON, nullable=True)
    filter_policy = Column(name='filter_policy', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)