from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsKinesisConsumer(Base):
    __tablename__ = 'aws_kinesis_consumer'
    consumer_name = Column(Text, name='consumer_name', nullable=True)
    consumer_arn = Column(Text, name='consumer_arn', nullable=True)
    stream_arn = Column(Text, name='stream_arn', nullable=True)
    consumer_status = Column(Text, name='consumer_status', nullable=True)
    consumer_creation_timestamp = Column(TIMESTAMP, name='consumer_creation_timestamp', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)