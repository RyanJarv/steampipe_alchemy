from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsKinesisConsumer(Base, FormatMixins):
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


# Local materialized view table
class AwsKinesisConsumerLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_kinesis_consumer_local'
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


cache = select(AwsKinesisConsumer).select_from(AwsKinesisConsumer)
create_materialized_view('aws_kinesis_consumer_local', cache, db.metadata_materialized)
