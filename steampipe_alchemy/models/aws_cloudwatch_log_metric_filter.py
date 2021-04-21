from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudwatchLogMetricFilter(Base):
    __tablename__ = 'aws_cloudwatch_log_metric_filter'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    log_group_name = Column(name='log_group_name', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    filter_pattern = Column(name='filter_pattern', type_=Text, nullable=True)
    metric_transformation_name = Column(name='metric_transformation_name', type_=Text, nullable=True)
    metric_transformation_namespace = Column(name='metric_transformation_namespace', type_=Text, nullable=True)
    metric_transformation_value = Column(name='metric_transformation_value', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)