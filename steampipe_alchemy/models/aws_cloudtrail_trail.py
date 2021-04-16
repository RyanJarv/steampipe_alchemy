from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsCloudtrailTrail(Base):
    __tablename__ = 'aws_cloudtrail_trail'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    home_region = Column(Text, name='home_region', nullable=True)
    is_multi_region_trail = Column(Boolean, name='is_multi_region_trail', nullable=True)
    log_file_validation_enabled = Column(Boolean, name='log_file_validation_enabled', nullable=True)
    is_logging = Column(Boolean, name='is_logging', nullable=True)
    log_group_arn = Column(Text, name='log_group_arn', nullable=True)
    cloudwatch_logs_role_arn = Column(Text, name='cloudwatch_logs_role_arn', nullable=True)
    has_custom_event_selectors = Column(Boolean, name='has_custom_event_selectors', nullable=True)
    has_insight_selectors = Column(Boolean, name='has_insight_selectors', nullable=True)
    include_global_service_events = Column(Boolean, name='include_global_service_events', nullable=True)
    is_organization_trail = Column(Boolean, name='is_organization_trail', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    s3_bucket_name = Column(Text, name='s3_bucket_name', nullable=True)
    s3_key_prefix = Column(Text, name='s3_key_prefix', nullable=True)
    sns_topic_arn = Column(Text, name='sns_topic_arn', nullable=True)
    latest_cloudwatch_logs_delivery_error = Column(Text, name='latest_cloudwatch_logs_delivery_error', nullable=True)
    latest_cloudwatch_logs_delivery_time = Column(TIMESTAMP, name='latest_cloudwatch_logs_delivery_time', nullable=True)
    latest_delivery_error = Column(Text, name='latest_delivery_error', nullable=True)
    latest_delivery_time = Column(TIMESTAMP, name='latest_delivery_time', nullable=True)
    latest_digest_delivery_error = Column(Text, name='latest_digest_delivery_error', nullable=True)
    latest_digest_delivery_time = Column(TIMESTAMP, name='latest_digest_delivery_time', nullable=True)
    latest_notification_error = Column(Text, name='latest_notification_error', nullable=True)
    latest_notification_time = Column(TIMESTAMP, name='latest_notification_time', nullable=True)
    start_logging_time = Column(TIMESTAMP, name='start_logging_time', nullable=True)
    stop_logging_time = Column(TIMESTAMP, name='stop_logging_time', nullable=True)
    advanced_event_selectors = Column(JSON, name='advanced_event_selectors', nullable=True)
    event_selectors = Column(JSON, name='event_selectors', nullable=True)
    insight_selectors = Column(JSON, name='insight_selectors', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    title = Column(Text, name='title', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)