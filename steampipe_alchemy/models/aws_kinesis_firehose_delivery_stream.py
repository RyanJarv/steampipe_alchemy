from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsKinesisFirehoseDeliveryStream(Base):
    __tablename__ = 'aws_kinesis_firehose_delivery_stream'
    delivery_stream_name = Column(name='delivery_stream_name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    delivery_stream_status = Column(name='delivery_stream_status', type_=Text, nullable=True)
    delivery_stream_type = Column(name='delivery_stream_type', type_=Text, nullable=True)
    version_id = Column(name='version_id', type_=Text, nullable=True)
    create_timestamp = Column(name='create_timestamp', type_=TIMESTAMP, nullable=True)
    has_more_destinations = Column(name='has_more_destinations', type_=Boolean, nullable=True)
    last_update_timestamp = Column(name='last_update_timestamp', type_=TIMESTAMP, nullable=True)
    delivery_stream_encryption_configuration = Column(name='delivery_stream_encryption_configuration', type_=JSON, nullable=True)
    destinations = Column(name='destinations', type_=JSON, nullable=True)
    failure_description = Column(name='failure_description', type_=JSON, nullable=True)
    source = Column(name='source', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)