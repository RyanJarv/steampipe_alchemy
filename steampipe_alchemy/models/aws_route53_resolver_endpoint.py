from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRoute53ResolverEndpoint(Base):
    __tablename__ = 'aws_route53_resolver_endpoint'
    name = Column(name='name', type_=Text, nullable=True)
    id = Column(name='id', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    creation_time = Column(name='creation_time', type_=Text, nullable=True)
    creator_request_id = Column(name='creator_request_id', type_=Text, nullable=True)
    direction = Column(name='direction', type_=Text, nullable=True)
    host_vpc_id = Column(name='host_vpc_id', type_=Text, nullable=True)
    ip_address_count = Column(name='ip_address_count', type_=BigInteger, nullable=True)
    modification_time = Column(name='modification_time', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    status_message = Column(name='status_message', type_=Text, nullable=True)
    ip_addresses = Column(name='ip_addresses', type_=JSON, nullable=True)
    security_group_ids = Column(name='security_group_ids', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)