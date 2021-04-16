from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSqsQueue(Base):
    __tablename__ = 'aws_sqs_queue'
    queue_url = Column(Text, name='queue_url', nullable=True)
    queue_arn = Column(Text, name='queue_arn', nullable=True)
    fifo_queue = Column(Boolean, name='fifo_queue', nullable=True)
    delay_seconds = Column(Text, name='delay_seconds', nullable=True)
    max_message_size = Column(Text, name='max_message_size', nullable=True)
    message_retention_seconds = Column(Text, name='message_retention_seconds', nullable=True)
    receive_wait_time_seconds = Column(Text, name='receive_wait_time_seconds', nullable=True)
    visibility_timeout_seconds = Column(Text, name='visibility_timeout_seconds', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    redrive_policy = Column(JSON, name='redrive_policy', nullable=True)
    content_based_deduplication = Column(Text, name='content_based_deduplication', nullable=True)
    kms_master_key_id = Column(Text, name='kms_master_key_id', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)