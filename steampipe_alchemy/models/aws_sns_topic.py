from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSnsTopic(Base):
    __tablename__ = 'aws_sns_topic'
    topic_arn = Column(name='topic_arn', type_=Text, nullable=True)
    display_name = Column(name='display_name', type_=Text, nullable=True)
    owner = Column(name='owner', type_=Text, nullable=True)
    subscriptions_confirmed = Column(name='subscriptions_confirmed', type_=BigInteger, nullable=True)
    subscriptions_deleted = Column(name='subscriptions_deleted', type_=BigInteger, nullable=True)
    subscriptions_pending = Column(name='subscriptions_pending', type_=BigInteger, nullable=True)
    kms_master_key_id = Column(name='kms_master_key_id', type_=Text, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    delivery_policy = Column(name='delivery_policy', type_=JSON, nullable=True)
    effective_delivery_policy = Column(name='effective_delivery_policy', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)