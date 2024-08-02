from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSnsTopic(Base, FormatMixins):
    __tablename__ = 'aws_sns_topic'
    _ctx = Column('_ctx', JSON, nullable=True)
    subscriptions_confirmed = Column('subscriptions_confirmed', BigInteger, nullable=True)
    subscriptions_deleted = Column('subscriptions_deleted', BigInteger, nullable=True)
    subscriptions_pending = Column('subscriptions_pending', BigInteger, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    delivery_policy = Column('delivery_policy', JSON, nullable=True)
    effective_delivery_policy = Column('effective_delivery_policy', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    lambda_success_feedback_role_arn = Column('lambda_success_feedback_role_arn', Text, nullable=True)
    lambda_success_feedback_sample_rate = Column('lambda_success_feedback_sample_rate', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    sqs_failure_feedback_role_arn = Column('sqs_failure_feedback_role_arn', Text, nullable=True)
    sqs_success_feedback_role_arn = Column('sqs_success_feedback_role_arn', Text, nullable=True)
    sqs_success_feedback_sample_rate = Column('sqs_success_feedback_sample_rate', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    kms_master_key_id = Column('kms_master_key_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    topic_arn = Column('topic_arn', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    display_name = Column('display_name', Text, nullable=True)
    application_failure_feedback_role_arn = Column('application_failure_feedback_role_arn', Text, nullable=True)
    application_success_feedback_role_arn = Column('application_success_feedback_role_arn', Text, nullable=True)
    application_success_feedback_sample_rate = Column('application_success_feedback_sample_rate', Text, nullable=True)
    firehose_failure_feedback_role_arn = Column('firehose_failure_feedback_role_arn', Text, nullable=True)
    firehose_success_feedback_role_arn = Column('firehose_success_feedback_role_arn', Text, nullable=True)
    firehose_success_feedback_sample_rate = Column('firehose_success_feedback_sample_rate', Text, nullable=True)
    http_failure_feedback_role_arn = Column('http_failure_feedback_role_arn', Text, nullable=True)
    http_success_feedback_role_arn = Column('http_success_feedback_role_arn', Text, nullable=True)
    http_success_feedback_sample_rate = Column('http_success_feedback_sample_rate', Text, nullable=True)
    lambda_failure_feedback_role_arn = Column('lambda_failure_feedback_role_arn', Text, nullable=True)