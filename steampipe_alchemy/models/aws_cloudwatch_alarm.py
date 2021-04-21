from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudwatchAlarm(Base):
    __tablename__ = 'aws_cloudwatch_alarm'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    alarm_arn = Column(name='alarm_arn', type_=Text, nullable=True)
    state_value = Column(name='state_value', type_=Text, nullable=True)
    actions_enabled = Column(name='actions_enabled', type_=Boolean, nullable=True)
    alarm_configuration_updated_timestamp = Column(name='alarm_configuration_updated_timestamp', type_=TIMESTAMP, nullable=True)
    alarm_description = Column(name='alarm_description', type_=Text, nullable=True)
    comparison_operator = Column(name='comparison_operator', type_=Text, nullable=True)
    datapoints_to_alarm = Column(name='datapoints_to_alarm', type_=BigInteger, nullable=True)
    evaluate_low_sample_count_percentile = Column(name='evaluate_low_sample_count_percentile', type_=Text, nullable=True)
    evaluation_periods = Column(name='evaluation_periods', type_=BigInteger, nullable=True)
    extended_statistic = Column(name='extended_statistic', type_=Text, nullable=True)
    metric_name = Column(name='metric_name', type_=Text, nullable=True)
    namespace = Column(name='namespace', type_=Text, nullable=True)
    period = Column(name='period', type_=BigInteger, nullable=True)
    state_reason = Column(name='state_reason', type_=Text, nullable=True)
    state_reason_data = Column(name='state_reason_data', type_=Text, nullable=True)
    state_updated_timestamp = Column(name='state_updated_timestamp', type_=TIMESTAMP, nullable=True)
    statistic = Column(name='statistic', type_=Text, nullable=True)
    threshold = Column(name='threshold', type_=psql.DOUBLE_PRECISION, nullable=True)
    threshold_metric_id = Column(name='threshold_metric_id', type_=Text, nullable=True)
    treat_missing_data = Column(name='treat_missing_data', type_=Text, nullable=True)
    unit = Column(name='unit', type_=Text, nullable=True)
    alarm_actions = Column(name='alarm_actions', type_=JSON, nullable=True)
    dimensions = Column(name='dimensions', type_=JSON, nullable=True)
    insufficient_data_actions = Column(name='insufficient_data_actions', type_=JSON, nullable=True)
    metrics = Column(name='metrics', type_=JSON, nullable=True)
    ok_actions = Column(name='ok_actions', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)