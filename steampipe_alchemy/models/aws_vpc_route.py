from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcRoute(Base):
    __tablename__ = 'aws_vpc_route'
    route_table_id = Column(Text, name='route_table_id', nullable=True)
    state = Column(Text, name='state', nullable=True)
    destination_cidr_block = Column(psql.CIDR, name='destination_cidr_block', nullable=True)
    destination_ipv6_cidr_block = Column(psql.CIDR, name='destination_ipv6_cidr_block', nullable=True)
    carrier_gateway_id = Column(Text, name='carrier_gateway_id', nullable=True)
    destination_prefix_list_id = Column(Text, name='destination_prefix_list_id', nullable=True)
    egress_only_internet_gateway_id = Column(Text, name='egress_only_internet_gateway_id', nullable=True)
    gateway_id = Column(Text, name='gateway_id', nullable=True)
    instance_id = Column(Text, name='instance_id', nullable=True)
    instance_owner_id = Column(Text, name='instance_owner_id', nullable=True)
    local_gateway_id = Column(Text, name='local_gateway_id', nullable=True)
    nat_gateway_id = Column(Text, name='nat_gateway_id', nullable=True)
    network_interface_id = Column(Text, name='network_interface_id', nullable=True)
    transit_gateway_id = Column(Text, name='transit_gateway_id', nullable=True)
    vpc_peering_connection_id = Column(Text, name='vpc_peering_connection_id', nullable=True)
    origin = Column(Text, name='origin', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)