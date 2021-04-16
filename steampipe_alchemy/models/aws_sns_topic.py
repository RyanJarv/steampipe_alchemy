from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSnsTopic(Base):
    __tablename__ = 'aws_sns_topic'
    topic_arn = Column(Text, name='topic_arn', nullable=True)
    display_name = Column(Text, name='display_name', nullable=True)
    owner = Column(Text, name='owner', nullable=True)
    subscriptions_confirmed = Column(BigInteger, name='subscriptions_confirmed', nullable=True)
    subscriptions_deleted = Column(BigInteger, name='subscriptions_deleted', nullable=True)
    subscriptions_pending = Column(BigInteger, name='subscriptions_pending', nullable=True)
    kms_master_key_id = Column(Text, name='kms_master_key_id', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    delivery_policy = Column(JSON, name='delivery_policy', nullable=True)
    effective_delivery_policy = Column(JSON, name='effective_delivery_policy', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)