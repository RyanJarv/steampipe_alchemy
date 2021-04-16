from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRedshiftEventSubscription(Base):
    __tablename__ = 'aws_redshift_event_subscription'
    cust_subscription_id = Column(Text, name='cust_subscription_id', nullable=True)
    customer_aws_id = Column(Text, name='customer_aws_id', nullable=True)
    enabled = Column(Boolean, name='enabled', nullable=True)
    severity = Column(Text, name='severity', nullable=True)
    sns_topic_arn = Column(Text, name='sns_topic_arn', nullable=True)
    source_type = Column(Text, name='source_type', nullable=True)
    status = Column(Text, name='status', nullable=True)
    subscription_creation_time = Column(TIMESTAMP, name='subscription_creation_time', nullable=True)
    event_categories_list = Column(JSON, name='event_categories_list', nullable=True)
    source_ids_list = Column(JSON, name='source_ids_list', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)