from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudwatchLogStream(Base, FormatMixins):
    __tablename__ = 'aws_cloudwatch_log_stream'
    _ctx = Column('_ctx', JSON, nullable=True)
    descending = Column('descending', Boolean, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    first_event_timestamp = Column('first_event_timestamp', TIMESTAMP, nullable=True)
    last_event_timestamp = Column('last_event_timestamp', TIMESTAMP, nullable=True)
    last_ingestion_time = Column('last_ingestion_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    upload_sequence_token = Column('upload_sequence_token', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    log_group_name = Column('log_group_name', Text, nullable=True)
    log_stream_name_prefix = Column('log_stream_name_prefix', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    order_by = Column('order_by', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)