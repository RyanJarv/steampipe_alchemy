from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudwatchLogGroup(Base):
    __tablename__ = 'aws_cloudwatch_log_group'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    metric_filter_count = Column(name='metric_filter_count', type_=BigInteger, nullable=True)
    retention_in_days = Column(name='retention_in_days', type_=BigInteger, nullable=True)
    stored_bytes = Column(name='stored_bytes', type_=BigInteger, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)