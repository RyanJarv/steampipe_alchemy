from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudwatchLogEvent(Base, FormatMixins):
    __tablename__ = 'aws_cloudwatch_log_event'
    _ctx = Column('_ctx', JSON, nullable=True)
    timestamp = Column('timestamp', TIMESTAMP, nullable=True)
    ingestion_time = Column('ingestion_time', TIMESTAMP, nullable=True)
    message_json = Column('message_json', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    filter = Column('filter', Text, nullable=True)
    message = Column('message', Text, nullable=True)
    log_group_name = Column('log_group_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    log_stream_name = Column('log_stream_name', Text, nullable=True)
    event_id = Column('event_id', Text, primary_key=True, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)