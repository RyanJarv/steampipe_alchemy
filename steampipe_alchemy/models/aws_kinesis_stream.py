from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsKinesisStream(Base):
    __tablename__ = 'aws_kinesis_stream'
    stream_name = Column(Text, name='stream_name', nullable=True)
    stream_arn = Column(Text, name='stream_arn', nullable=True)
    stream_status = Column(Text, name='stream_status', nullable=True)
    stream_creation_timestamp = Column(TIMESTAMP, name='stream_creation_timestamp', nullable=True)
    encryption_type = Column(Text, name='encryption_type', nullable=True)
    key_id = Column(Text, name='key_id', nullable=True)
    retention_period_hours = Column(BigInteger, name='retention_period_hours', nullable=True)
    consumer_count = Column(BigInteger, name='consumer_count', nullable=True)
    open_shard_count = Column(BigInteger, name='open_shard_count', nullable=True)
    has_more_shards = Column(Boolean, name='has_more_shards', nullable=True)
    shards = Column(JSON, name='shards', nullable=True)
    enhanced_monitoring = Column(JSON, name='enhanced_monitoring', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)