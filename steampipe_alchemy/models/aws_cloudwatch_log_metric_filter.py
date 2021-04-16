from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsCloudwatchLogMetricFilter(Base):
    __tablename__ = 'aws_cloudwatch_log_metric_filter'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    log_group_name = Column(Text, name='log_group_name', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    filter_pattern = Column(Text, name='filter_pattern', nullable=True)
    metric_transformation_name = Column(Text, name='metric_transformation_name', nullable=True)
    metric_transformation_namespace = Column(Text, name='metric_transformation_namespace', nullable=True)
    metric_transformation_value = Column(Text, name='metric_transformation_value', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)