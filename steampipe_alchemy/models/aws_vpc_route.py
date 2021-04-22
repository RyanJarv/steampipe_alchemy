from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcRoute(Base):
    __tablename__ = 'aws_vpc_route'
    route_table_id = Column('route_table_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    destination_cidr_block = Column('destination_cidr_block', psql.CIDR, nullable=True)
    destination_ipv6_cidr_block = Column('destination_ipv6_cidr_block', psql.CIDR, nullable=True)
    carrier_gateway_id = Column('carrier_gateway_id', Text, nullable=True)
    destination_prefix_list_id = Column('destination_prefix_list_id', Text, nullable=True)
    egress_only_internet_gateway_id = Column('egress_only_internet_gateway_id', Text, nullable=True)
    gateway_id = Column('gateway_id', Text, nullable=True)
    instance_id = Column('instance_id', Text, nullable=True)
    instance_owner_id = Column('instance_owner_id', Text, nullable=True)
    local_gateway_id = Column('local_gateway_id', Text, nullable=True)
    nat_gateway_id = Column('nat_gateway_id', Text, nullable=True)
    network_interface_id = Column('network_interface_id', Text, nullable=True)
    transit_gateway_id = Column('transit_gateway_id', Text, nullable=True)
    vpc_peering_connection_id = Column('vpc_peering_connection_id', Text, nullable=True)
    origin = Column('origin', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)