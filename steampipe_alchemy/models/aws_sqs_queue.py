from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSqsQueue(Base, FormatMixins):
    __tablename__ = 'aws_sqs_queue'
    _ctx = Column('_ctx', JSON, nullable=True)
    fifo_queue = Column('fifo_queue', Boolean, nullable=True)
    sqs_managed_sse_enabled = Column('sqs_managed_sse_enabled', Boolean, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    redrive_policy = Column('redrive_policy', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    visibility_timeout_seconds = Column('visibility_timeout_seconds', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    content_based_deduplication = Column('content_based_deduplication', Text, nullable=True)
    deduplication_scope = Column('deduplication_scope', Text, nullable=True)
    kms_master_key_id = Column('kms_master_key_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    queue_arn = Column('queue_arn', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    fifo_throughput_limit = Column('fifo_throughput_limit', Text, nullable=True)
    delay_seconds = Column('delay_seconds', Text, nullable=True)
    max_message_size = Column('max_message_size', Text, nullable=True)
    message_retention_seconds = Column('message_retention_seconds', Text, nullable=True)
    receive_wait_time_seconds = Column('receive_wait_time_seconds', Text, nullable=True)
    queue_url = Column('queue_url', Text, nullable=True)