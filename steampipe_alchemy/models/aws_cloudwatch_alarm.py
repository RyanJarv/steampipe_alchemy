from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsCloudwatchAlarm(Base):
    __tablename__ = 'aws_cloudwatch_alarm'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    alarm_arn = Column(Text, name='alarm_arn', nullable=True)
    state_value = Column(Text, name='state_value', nullable=True)
    actions_enabled = Column(Boolean, name='actions_enabled', nullable=True)
    alarm_configuration_updated_timestamp = Column(TIMESTAMP, name='alarm_configuration_updated_timestamp', nullable=True)
    alarm_description = Column(Text, name='alarm_description', nullable=True)
    comparison_operator = Column(Text, name='comparison_operator', nullable=True)
    datapoints_to_alarm = Column(BigInteger, name='datapoints_to_alarm', nullable=True)
    evaluate_low_sample_count_percentile = Column(Text, name='evaluate_low_sample_count_percentile', nullable=True)
    evaluation_periods = Column(BigInteger, name='evaluation_periods', nullable=True)
    extended_statistic = Column(Text, name='extended_statistic', nullable=True)
    metric_name = Column(Text, name='metric_name', nullable=True)
    namespace = Column(Text, name='namespace', nullable=True)
    period = Column(BigInteger, name='period', nullable=True)
    state_reason = Column(Text, name='state_reason', nullable=True)
    state_reason_data = Column(Text, name='state_reason_data', nullable=True)
    state_updated_timestamp = Column(TIMESTAMP, name='state_updated_timestamp', nullable=True)
    statistic = Column(Text, name='statistic', nullable=True)
    threshold = Column(psql.DOUBLE_PRECISION, name='threshold', nullable=True)
    threshold_metric_id = Column(Text, name='threshold_metric_id', nullable=True)
    treat_missing_data = Column(Text, name='treat_missing_data', nullable=True)
    unit = Column(Text, name='unit', nullable=True)
    alarm_actions = Column(JSON, name='alarm_actions', nullable=True)
    dimensions = Column(JSON, name='dimensions', nullable=True)
    insufficient_data_actions = Column(JSON, name='insufficient_data_actions', nullable=True)
    metrics = Column(JSON, name='metrics', nullable=True)
    ok_actions = Column(JSON, name='ok_actions', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)