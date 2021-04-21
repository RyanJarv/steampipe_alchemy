from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRedshiftEventSubscription(Base):
    __tablename__ = 'aws_redshift_event_subscription'
    cust_subscription_id = Column(name='cust_subscription_id', type_=Text, nullable=True)
    customer_aws_id = Column(name='customer_aws_id', type_=Text, nullable=True)
    enabled = Column(name='enabled', type_=Boolean, nullable=True)
    severity = Column(name='severity', type_=Text, nullable=True)
    sns_topic_arn = Column(name='sns_topic_arn', type_=Text, nullable=True)
    source_type = Column(name='source_type', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    subscription_creation_time = Column(name='subscription_creation_time', type_=TIMESTAMP, nullable=True)
    event_categories_list = Column(name='event_categories_list', type_=JSON, nullable=True)
    source_ids_list = Column(name='source_ids_list', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)