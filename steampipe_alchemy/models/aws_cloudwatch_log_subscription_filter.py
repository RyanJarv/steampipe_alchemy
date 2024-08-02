from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudwatchLogSubscriptionFilter(Base, FormatMixins):
    __tablename__ = 'aws_cloudwatch_log_subscription_filter'
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    filter_pattern = Column('filter_pattern', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    log_group_name = Column('log_group_name', Text, nullable=True)
    destination_arn = Column('destination_arn', Text, nullable=True)
    distribution = Column('distribution', Text, nullable=True)