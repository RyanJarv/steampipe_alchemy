from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsKinesisFirehoseDeliveryStream(Base):
    __tablename__ = 'aws_kinesis_firehose_delivery_stream'
    delivery_stream_name = Column('delivery_stream_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    delivery_stream_status = Column('delivery_stream_status', Text, nullable=True)
    delivery_stream_type = Column('delivery_stream_type', Text, nullable=True)
    version_id = Column('version_id', Text, nullable=True)
    create_timestamp = Column('create_timestamp', TIMESTAMP, nullable=True)
    has_more_destinations = Column('has_more_destinations', Boolean, nullable=True)
    last_update_timestamp = Column('last_update_timestamp', TIMESTAMP, nullable=True)
    delivery_stream_encryption_configuration = Column('delivery_stream_encryption_configuration', JSON, nullable=True)
    destinations = Column('destinations', JSON, nullable=True)
    failure_description = Column('failure_description', JSON, nullable=True)
    source = Column('source', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)