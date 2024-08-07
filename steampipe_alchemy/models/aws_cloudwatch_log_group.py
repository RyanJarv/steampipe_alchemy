from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudwatchLogGroup(Base, FormatMixins):
    __tablename__ = 'aws_cloudwatch_log_group'
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    metric_filter_count = Column('metric_filter_count', BigInteger, nullable=True)
    retention_in_days = Column('retention_in_days', BigInteger, nullable=True)
    stored_bytes = Column('stored_bytes', BigInteger, nullable=True)
    data_protection = Column('data_protection', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    data_protection_policy = Column('data_protection_policy', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)