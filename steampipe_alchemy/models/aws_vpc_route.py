from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcRoute(Base):
    __tablename__ = 'aws_vpc_route'
    route_table_id = Column(name='route_table_id', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    destination_cidr_block = Column(name='destination_cidr_block', type_=psql.CIDR, nullable=True)
    destination_ipv6_cidr_block = Column(name='destination_ipv6_cidr_block', type_=psql.CIDR, nullable=True)
    carrier_gateway_id = Column(name='carrier_gateway_id', type_=Text, nullable=True)
    destination_prefix_list_id = Column(name='destination_prefix_list_id', type_=Text, nullable=True)
    egress_only_internet_gateway_id = Column(name='egress_only_internet_gateway_id', type_=Text, nullable=True)
    gateway_id = Column(name='gateway_id', type_=Text, nullable=True)
    instance_id = Column(name='instance_id', type_=Text, nullable=True)
    instance_owner_id = Column(name='instance_owner_id', type_=Text, nullable=True)
    local_gateway_id = Column(name='local_gateway_id', type_=Text, nullable=True)
    nat_gateway_id = Column(name='nat_gateway_id', type_=Text, nullable=True)
    network_interface_id = Column(name='network_interface_id', type_=Text, nullable=True)
    transit_gateway_id = Column(name='transit_gateway_id', type_=Text, nullable=True)
    vpc_peering_connection_id = Column(name='vpc_peering_connection_id', type_=Text, nullable=True)
    origin = Column(name='origin', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)