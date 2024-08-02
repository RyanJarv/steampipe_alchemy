from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudtrailTrailEvent(Base, FormatMixins):
    __tablename__ = 'aws_cloudtrail_trail_event'
    additional_event_data = Column('additional_event_data', JSON, nullable=True)
    cloudtrail_event = Column('cloudtrail_event', JSON, nullable=True)
    request_parameters = Column('request_parameters', JSON, nullable=True)
    response_elements = Column('response_elements', JSON, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    tls_details = Column('tls_details', JSON, nullable=True)
    user_identity = Column('user_identity', JSON, nullable=True)
    timestamp = Column('timestamp', TIMESTAMP, nullable=True)
    timestamp_ms = Column('timestamp_ms', BigInteger, nullable=True)
    read_only = Column('read_only', Boolean, nullable=True)
    event_time = Column('event_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    recipient_account_id = Column('recipient_account_id', Text, nullable=True)
    request_id = Column('request_id', Text, nullable=True)
    filter = Column('filter', Text, nullable=True)
    source_ip_address = Column('source_ip_address', Text, nullable=True)
    user_agent = Column('user_agent', Text, nullable=True)
    user_type = Column('user_type', Text, nullable=True)
    username = Column('username', Text, nullable=True)
    user_identifier = Column('user_identifier', Text, nullable=True)
    vpc_endpoint_id = Column('vpc_endpoint_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    shared_event_id = Column('shared_event_id', Text, nullable=True)
    log_group_name = Column('log_group_name', Text, nullable=True)
    log_stream_name = Column('log_stream_name', Text, nullable=True)
    access_key_id = Column('access_key_id', Text, nullable=True)
    aws_region = Column('aws_region', Text, nullable=True)
    error_code = Column('error_code', Text, nullable=True)
    error_message = Column('error_message', Text, nullable=True)
    event_category = Column('event_category', Text, nullable=True)
    event_id = Column('event_id', Text, primary_key=True, nullable=True)
    event_name = Column('event_name', Text, nullable=True)
    event_source = Column('event_source', Text, nullable=True)
    event_type = Column('event_type', Text, nullable=True)
    event_version = Column('event_version', Text, nullable=True)