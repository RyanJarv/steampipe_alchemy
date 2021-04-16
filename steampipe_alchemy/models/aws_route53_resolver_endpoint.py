from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRoute53ResolverEndpoint(Base):
    __tablename__ = 'aws_route53_resolver_endpoint'
    name = Column(Text, name='name', nullable=True)
    id = Column(Text, name='id', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    creation_time = Column(Text, name='creation_time', nullable=True)
    creator_request_id = Column(Text, name='creator_request_id', nullable=True)
    direction = Column(Text, name='direction', nullable=True)
    host_vpc_id = Column(Text, name='host_vpc_id', nullable=True)
    ip_address_count = Column(BigInteger, name='ip_address_count', nullable=True)
    modification_time = Column(Text, name='modification_time', nullable=True)
    status = Column(Text, name='status', nullable=True)
    status_message = Column(Text, name='status_message', nullable=True)
    ip_addresses = Column(JSON, name='ip_addresses', nullable=True)
    security_group_ids = Column(JSON, name='security_group_ids', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)