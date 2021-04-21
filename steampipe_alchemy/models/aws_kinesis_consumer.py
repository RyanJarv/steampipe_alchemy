from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsKinesisConsumer(Base):
    __tablename__ = 'aws_kinesis_consumer'
    consumer_name = Column(name='consumer_name', type_=Text, nullable=True)
    consumer_arn = Column(name='consumer_arn', type_=Text, nullable=True)
    stream_arn = Column(name='stream_arn', type_=Text, nullable=True)
    consumer_status = Column(name='consumer_status', type_=Text, nullable=True)
    consumer_creation_timestamp = Column(name='consumer_creation_timestamp', type_=TIMESTAMP, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)