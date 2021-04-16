from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsCloudwatchLogGroup(Base):
    __tablename__ = 'aws_cloudwatch_log_group'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    metric_filter_count = Column(BigInteger, name='metric_filter_count', nullable=True)
    retention_in_days = Column(BigInteger, name='retention_in_days', nullable=True)
    stored_bytes = Column(BigInteger, name='stored_bytes', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)