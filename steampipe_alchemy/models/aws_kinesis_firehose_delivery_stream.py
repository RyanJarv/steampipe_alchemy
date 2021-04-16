from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsKinesisFirehoseDeliveryStream(Base):
    __tablename__ = 'aws_kinesis_firehose_delivery_stream'
    delivery_stream_name = Column(Text, name='delivery_stream_name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    delivery_stream_status = Column(Text, name='delivery_stream_status', nullable=True)
    delivery_stream_type = Column(Text, name='delivery_stream_type', nullable=True)
    version_id = Column(Text, name='version_id', nullable=True)
    create_timestamp = Column(TIMESTAMP, name='create_timestamp', nullable=True)
    has_more_destinations = Column(Boolean, name='has_more_destinations', nullable=True)
    last_update_timestamp = Column(TIMESTAMP, name='last_update_timestamp', nullable=True)
    delivery_stream_encryption_configuration = Column(JSON, name='delivery_stream_encryption_configuration', nullable=True)
    destinations = Column(JSON, name='destinations', nullable=True)
    failure_description = Column(JSON, name='failure_description', nullable=True)
    source = Column(JSON, name='source', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)