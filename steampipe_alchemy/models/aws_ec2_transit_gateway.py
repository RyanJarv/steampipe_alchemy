from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2TransitGateway(Base):
    __tablename__ = 'aws_ec2_transit_gateway'
    transit_gateway_id = Column(name='transit_gateway_id', type_=Text, nullable=True)
    transit_gateway_arn = Column(name='transit_gateway_arn', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    amazon_side_asn = Column(name='amazon_side_asn', type_=BigInteger, nullable=True)
    association_default_route_table_id = Column(name='association_default_route_table_id', type_=Text, nullable=True)
    auto_accept_shared_attachments = Column(name='auto_accept_shared_attachments', type_=Text, nullable=True)
    default_route_table_association = Column(name='default_route_table_association', type_=Text, nullable=True)
    default_route_table_propagation = Column(name='default_route_table_propagation', type_=Text, nullable=True)
    dns_support = Column(name='dns_support', type_=Text, nullable=True)
    multicast_support = Column(name='multicast_support', type_=Text, nullable=True)
    propagation_default_route_table_id = Column(name='propagation_default_route_table_id', type_=Text, nullable=True)
    vpn_ecmp_support = Column(name='vpn_ecmp_support', type_=Text, nullable=True)
    cidr_blocks = Column(name='cidr_blocks', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)