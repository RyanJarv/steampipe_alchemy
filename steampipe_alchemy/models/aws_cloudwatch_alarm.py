from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudwatchAlarm(Base, FormatMixins):
    __tablename__ = 'aws_cloudwatch_alarm'
    _ctx = Column('_ctx', JSON, nullable=True)
    actions_enabled = Column('actions_enabled', Boolean, nullable=True)
    alarm_configuration_updated_timestamp = Column('alarm_configuration_updated_timestamp', TIMESTAMP, nullable=True)
    datapoints_to_alarm = Column('datapoints_to_alarm', BigInteger, nullable=True)
    evaluation_periods = Column('evaluation_periods', BigInteger, nullable=True)
    period = Column('period', BigInteger, nullable=True)
    state_updated_timestamp = Column('state_updated_timestamp', TIMESTAMP, nullable=True)
    threshold = Column('threshold', psql.DOUBLE_PRECISION, nullable=True)
    alarm_actions = Column('alarm_actions', JSON, nullable=True)
    dimensions = Column('dimensions', JSON, nullable=True)
    insufficient_data_actions = Column('insufficient_data_actions', JSON, nullable=True)
    metrics = Column('metrics', JSON, nullable=True)
    ok_actions = Column('ok_actions', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    statistic = Column('statistic', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    threshold_metric_id = Column('threshold_metric_id', Text, nullable=True)
    treat_missing_data = Column('treat_missing_data', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    state_value = Column('state_value', Text, nullable=True)
    unit = Column('unit', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    alarm_description = Column('alarm_description', Text, nullable=True)
    comparison_operator = Column('comparison_operator', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    evaluate_low_sample_count_percentile = Column('evaluate_low_sample_count_percentile', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    extended_statistic = Column('extended_statistic', Text, nullable=True)
    metric_name = Column('metric_name', Text, nullable=True)
    namespace = Column('namespace', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    state_reason = Column('state_reason', Text, nullable=True)
    state_reason_data = Column('state_reason_data', Text, nullable=True)
    region = Column('region', Text, nullable=True)