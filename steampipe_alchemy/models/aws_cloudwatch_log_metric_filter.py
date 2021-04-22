from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudwatchLogMetricFilter(Base):
    __tablename__ = 'aws_cloudwatch_log_metric_filter'
    name = Column('name', Text, primary_key=True, nullable=True)
    log_group_name = Column('log_group_name', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    filter_pattern = Column('filter_pattern', Text, nullable=True)
    metric_transformation_name = Column('metric_transformation_name', Text, nullable=True)
    metric_transformation_namespace = Column('metric_transformation_namespace', Text, nullable=True)
    metric_transformation_value = Column('metric_transformation_value', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)