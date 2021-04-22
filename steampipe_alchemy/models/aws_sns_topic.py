from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSnsTopic(Base):
    __tablename__ = 'aws_sns_topic'
    topic_arn = Column('topic_arn', Text, nullable=True)
    display_name = Column('display_name', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    subscriptions_confirmed = Column('subscriptions_confirmed', BigInteger, nullable=True)
    subscriptions_deleted = Column('subscriptions_deleted', BigInteger, nullable=True)
    subscriptions_pending = Column('subscriptions_pending', BigInteger, nullable=True)
    kms_master_key_id = Column('kms_master_key_id', Text, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    delivery_policy = Column('delivery_policy', JSON, nullable=True)
    effective_delivery_policy = Column('effective_delivery_policy', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)