from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudtrailTrail(Base):
    __tablename__ = 'aws_cloudtrail_trail'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    home_region = Column('home_region', Text, nullable=True)
    is_multi_region_trail = Column('is_multi_region_trail', Boolean, nullable=True)
    log_file_validation_enabled = Column('log_file_validation_enabled', Boolean, nullable=True)
    is_logging = Column('is_logging', Boolean, nullable=True)
    log_group_arn = Column('log_group_arn', Text, nullable=True)
    cloudwatch_logs_role_arn = Column('cloudwatch_logs_role_arn', Text, nullable=True)
    has_custom_event_selectors = Column('has_custom_event_selectors', Boolean, nullable=True)
    has_insight_selectors = Column('has_insight_selectors', Boolean, nullable=True)
    include_global_service_events = Column('include_global_service_events', Boolean, nullable=True)
    is_organization_trail = Column('is_organization_trail', Boolean, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    s3_bucket_name = Column('s3_bucket_name', Text, nullable=True)
    s3_key_prefix = Column('s3_key_prefix', Text, nullable=True)
    sns_topic_arn = Column('sns_topic_arn', Text, nullable=True)
    latest_cloudwatch_logs_delivery_error = Column('latest_cloudwatch_logs_delivery_error', Text, nullable=True)
    latest_cloudwatch_logs_delivery_time = Column('latest_cloudwatch_logs_delivery_time', TIMESTAMP, nullable=True)
    latest_delivery_error = Column('latest_delivery_error', Text, nullable=True)
    latest_delivery_time = Column('latest_delivery_time', TIMESTAMP, nullable=True)
    latest_digest_delivery_error = Column('latest_digest_delivery_error', Text, nullable=True)
    latest_digest_delivery_time = Column('latest_digest_delivery_time', TIMESTAMP, nullable=True)
    latest_notification_error = Column('latest_notification_error', Text, nullable=True)
    latest_notification_time = Column('latest_notification_time', TIMESTAMP, nullable=True)
    start_logging_time = Column('start_logging_time', TIMESTAMP, nullable=True)
    stop_logging_time = Column('stop_logging_time', TIMESTAMP, nullable=True)
    advanced_event_selectors = Column('advanced_event_selectors', JSON, nullable=True)
    event_selectors = Column('event_selectors', JSON, nullable=True)
    insight_selectors = Column('insight_selectors', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)