from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsKinesisConsumer(Base):
    __tablename__ = 'aws_kinesis_consumer'
    consumer_name = Column('consumer_name', Text, nullable=True)
    consumer_arn = Column('consumer_arn', Text, nullable=True)
    stream_arn = Column('stream_arn', Text, nullable=True)
    consumer_status = Column('consumer_status', Text, nullable=True)
    consumer_creation_timestamp = Column('consumer_creation_timestamp', TIMESTAMP, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)