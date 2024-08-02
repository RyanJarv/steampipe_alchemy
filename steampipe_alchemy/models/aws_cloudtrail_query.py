from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudtrailQuery(Base, FormatMixins):
    __tablename__ = 'aws_cloudtrail_query'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    bytes_scanned = Column('bytes_scanned', BigInteger, nullable=True)
    events_matched = Column('events_matched', BigInteger, nullable=True)
    events_scanned = Column('events_scanned', BigInteger, nullable=True)
    execution_time_in_millis = Column('execution_time_in_millis', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    query_id = Column('query_id', Text, nullable=True)
    query_string = Column('query_string', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    event_data_store_arn = Column('event_data_store_arn', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    delivery_s3_uri = Column('delivery_s3_uri', Text, nullable=True)
    delivery_status = Column('delivery_status', Text, nullable=True)
    error_message = Column('error_message', Text, nullable=True)
    query_status = Column('query_status', Text, nullable=True)