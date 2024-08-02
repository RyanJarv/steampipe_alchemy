from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDirectoryServiceLogSubscription(Base, FormatMixins):
    __tablename__ = 'aws_directory_service_log_subscription'
    subscription_created_date_time = Column('subscription_created_date_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    directory_id = Column('directory_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    log_group_name = Column('log_group_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)