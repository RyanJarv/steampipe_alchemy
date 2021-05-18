from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsCloudwatchLogGroup(Base, FormatMixins):
    __tablename__ = 'aws_cloudwatch_log_group'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    metric_filter_count = Column('metric_filter_count', BigInteger, nullable=True)
    retention_in_days = Column('retention_in_days', BigInteger, nullable=True)
    stored_bytes = Column('stored_bytes', BigInteger, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsCloudwatchLogGroupLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_cloudwatch_log_group_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    metric_filter_count = Column('metric_filter_count', BigInteger, nullable=True)
    retention_in_days = Column('retention_in_days', BigInteger, nullable=True)
    stored_bytes = Column('stored_bytes', BigInteger, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsCloudwatchLogGroup).select_from(AwsCloudwatchLogGroup)
create_materialized_view('aws_cloudwatch_log_group_local', cache, db.metadata_materialized)
