from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53ResolverEndpoint(Base, FormatMixins):
    __tablename__ = 'aws_route53_resolver_endpoint'
    ip_address_count = Column('ip_address_count', BigInteger, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    ip_addresses = Column('ip_addresses', JSON, nullable=True)
    security_group_ids = Column('security_group_ids', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    host_vpc_id = Column('host_vpc_id', Text, nullable=True)
    modification_time = Column('modification_time', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    creation_time = Column('creation_time', Text, nullable=True)
    creator_request_id = Column('creator_request_id', Text, nullable=True)
    direction = Column('direction', Text, nullable=True)