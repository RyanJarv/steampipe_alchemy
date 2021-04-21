from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsKinesisStream(Base):
    __tablename__ = 'aws_kinesis_stream'
    stream_name = Column(name='stream_name', type_=Text, nullable=True)
    stream_arn = Column(name='stream_arn', type_=Text, nullable=True)
    stream_status = Column(name='stream_status', type_=Text, nullable=True)
    stream_creation_timestamp = Column(name='stream_creation_timestamp', type_=TIMESTAMP, nullable=True)
    encryption_type = Column(name='encryption_type', type_=Text, nullable=True)
    key_id = Column(name='key_id', type_=Text, nullable=True)
    retention_period_hours = Column(name='retention_period_hours', type_=BigInteger, nullable=True)
    consumer_count = Column(name='consumer_count', type_=BigInteger, nullable=True)
    open_shard_count = Column(name='open_shard_count', type_=BigInteger, nullable=True)
    has_more_shards = Column(name='has_more_shards', type_=Boolean, nullable=True)
    shards = Column(name='shards', type_=JSON, nullable=True)
    enhanced_monitoring = Column(name='enhanced_monitoring', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)