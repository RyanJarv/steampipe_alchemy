from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudtrailTrail(Base):
    __tablename__ = 'aws_cloudtrail_trail'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    home_region = Column(name='home_region', type_=Text, nullable=True)
    is_multi_region_trail = Column(name='is_multi_region_trail', type_=Boolean, nullable=True)
    log_file_validation_enabled = Column(name='log_file_validation_enabled', type_=Boolean, nullable=True)
    is_logging = Column(name='is_logging', type_=Boolean, nullable=True)
    log_group_arn = Column(name='log_group_arn', type_=Text, nullable=True)
    cloudwatch_logs_role_arn = Column(name='cloudwatch_logs_role_arn', type_=Text, nullable=True)
    has_custom_event_selectors = Column(name='has_custom_event_selectors', type_=Boolean, nullable=True)
    has_insight_selectors = Column(name='has_insight_selectors', type_=Boolean, nullable=True)
    include_global_service_events = Column(name='include_global_service_events', type_=Boolean, nullable=True)
    is_organization_trail = Column(name='is_organization_trail', type_=Boolean, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    s3_bucket_name = Column(name='s3_bucket_name', type_=Text, nullable=True)
    s3_key_prefix = Column(name='s3_key_prefix', type_=Text, nullable=True)
    sns_topic_arn = Column(name='sns_topic_arn', type_=Text, nullable=True)
    latest_cloudwatch_logs_delivery_error = Column(name='latest_cloudwatch_logs_delivery_error', type_=Text, nullable=True)
    latest_cloudwatch_logs_delivery_time = Column(name='latest_cloudwatch_logs_delivery_time', type_=TIMESTAMP, nullable=True)
    latest_delivery_error = Column(name='latest_delivery_error', type_=Text, nullable=True)
    latest_delivery_time = Column(name='latest_delivery_time', type_=TIMESTAMP, nullable=True)
    latest_digest_delivery_error = Column(name='latest_digest_delivery_error', type_=Text, nullable=True)
    latest_digest_delivery_time = Column(name='latest_digest_delivery_time', type_=TIMESTAMP, nullable=True)
    latest_notification_error = Column(name='latest_notification_error', type_=Text, nullable=True)
    latest_notification_time = Column(name='latest_notification_time', type_=TIMESTAMP, nullable=True)
    start_logging_time = Column(name='start_logging_time', type_=TIMESTAMP, nullable=True)
    stop_logging_time = Column(name='stop_logging_time', type_=TIMESTAMP, nullable=True)
    advanced_event_selectors = Column(name='advanced_event_selectors', type_=JSON, nullable=True)
    event_selectors = Column(name='event_selectors', type_=JSON, nullable=True)
    insight_selectors = Column(name='insight_selectors', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)