from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53ResolverQueryLogConfig(Base, FormatMixins):
    __tablename__ = 'aws_route53_resolver_query_log_config'
    ip_address_count = Column('ip_address_count', BigInteger, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    association_count = Column('association_count', BigInteger, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    id = Column('id', Text, nullable=True)
    share_status = Column('share_status', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    creator_request_id = Column('creator_request_id', Text, nullable=True)
    destination_arn = Column('destination_arn', Text, nullable=True)