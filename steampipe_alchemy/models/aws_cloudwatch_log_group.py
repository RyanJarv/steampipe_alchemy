from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudwatchLogGroup(Base, FormatMixins):
    __tablename__ = 'aws_cloudwatch_log_group'
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    metric_filter_count = Column('metric_filter_count', BigInteger, nullable=True)
    retention_in_days = Column('retention_in_days', BigInteger, nullable=True)
    stored_bytes = Column('stored_bytes', BigInteger, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)