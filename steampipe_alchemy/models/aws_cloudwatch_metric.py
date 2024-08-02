from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudwatchMetric(Base, FormatMixins):
    __tablename__ = 'aws_cloudwatch_metric'
    dimensions = Column('dimensions', JSON, nullable=True)
    dimensions_filter = Column('dimensions_filter', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    namespace = Column('namespace', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    metric_name = Column('metric_name', Text, nullable=True)