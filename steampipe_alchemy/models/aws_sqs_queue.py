from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSqsQueue(Base):
    __tablename__ = 'aws_sqs_queue'
    queue_url = Column(name='queue_url', type_=Text, nullable=True)
    queue_arn = Column(name='queue_arn', type_=Text, nullable=True)
    fifo_queue = Column(name='fifo_queue', type_=Boolean, nullable=True)
    delay_seconds = Column(name='delay_seconds', type_=Text, nullable=True)
    max_message_size = Column(name='max_message_size', type_=Text, nullable=True)
    message_retention_seconds = Column(name='message_retention_seconds', type_=Text, nullable=True)
    receive_wait_time_seconds = Column(name='receive_wait_time_seconds', type_=Text, nullable=True)
    visibility_timeout_seconds = Column(name='visibility_timeout_seconds', type_=Text, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    redrive_policy = Column(name='redrive_policy', type_=JSON, nullable=True)
    content_based_deduplication = Column(name='content_based_deduplication', type_=Text, nullable=True)
    kms_master_key_id = Column(name='kms_master_key_id', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)