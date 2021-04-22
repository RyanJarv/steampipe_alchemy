from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsKinesisStream(Base):
    __tablename__ = 'aws_kinesis_stream'
    stream_name = Column('stream_name', Text, nullable=True)
    stream_arn = Column('stream_arn', Text, nullable=True)
    stream_status = Column('stream_status', Text, nullable=True)
    stream_creation_timestamp = Column('stream_creation_timestamp', TIMESTAMP, nullable=True)
    encryption_type = Column('encryption_type', Text, nullable=True)
    key_id = Column('key_id', Text, nullable=True)
    retention_period_hours = Column('retention_period_hours', BigInteger, nullable=True)
    consumer_count = Column('consumer_count', BigInteger, nullable=True)
    open_shard_count = Column('open_shard_count', BigInteger, nullable=True)
    has_more_shards = Column('has_more_shards', Boolean, nullable=True)
    shards = Column('shards', JSON, nullable=True)
    enhanced_monitoring = Column('enhanced_monitoring', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)