from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2TransitGateway(Base):
    __tablename__ = 'aws_ec2_transit_gateway'
    transit_gateway_id = Column(Text, name='transit_gateway_id', nullable=True)
    transit_gateway_arn = Column(Text, name='transit_gateway_arn', nullable=True)
    state = Column(Text, name='state', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    description = Column(Text, name='description', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    amazon_side_asn = Column(BigInteger, name='amazon_side_asn', nullable=True)
    association_default_route_table_id = Column(Text, name='association_default_route_table_id', nullable=True)
    auto_accept_shared_attachments = Column(Text, name='auto_accept_shared_attachments', nullable=True)
    default_route_table_association = Column(Text, name='default_route_table_association', nullable=True)
    default_route_table_propagation = Column(Text, name='default_route_table_propagation', nullable=True)
    dns_support = Column(Text, name='dns_support', nullable=True)
    multicast_support = Column(Text, name='multicast_support', nullable=True)
    propagation_default_route_table_id = Column(Text, name='propagation_default_route_table_id', nullable=True)
    vpn_ecmp_support = Column(Text, name='vpn_ecmp_support', nullable=True)
    cidr_blocks = Column(JSON, name='cidr_blocks', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)