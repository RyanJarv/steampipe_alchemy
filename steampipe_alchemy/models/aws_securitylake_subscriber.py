from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSecuritylakeSubscriber(Base, FormatMixins):
    __tablename__ = 'aws_securitylake_subscriber'
    akas = Column('akas', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    access_types = Column('access_types', JSON, nullable=True)
    source_types = Column('source_types', JSON, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    subscriber_description = Column('subscriber_description', Text, nullable=True)
    subscription_endpoint = Column('subscription_endpoint', Text, nullable=True)
    subscriber_name = Column('subscriber_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    subscription_protocol = Column('subscription_protocol', Text, nullable=True)
    subscription_id = Column('subscription_id', Text, nullable=True)
    subscription_status = Column('subscription_status', Text, nullable=True)
    external_id = Column('external_id', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    s3_bucket_arn = Column('s3_bucket_arn', Text, nullable=True)
    sns_arn = Column('sns_arn', Text, nullable=True)