from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2TransitGatewayRouteTable(Base):
    __tablename__ = 'aws_ec2_transit_gateway_route_table'
    transit_gateway_route_table_id = Column(Text, name='transit_gateway_route_table_id', nullable=True)
    transit_gateway_id = Column(Text, name='transit_gateway_id', nullable=True)
    state = Column(Text, name='state', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    default_association_route_table = Column(Boolean, name='default_association_route_table', nullable=True)
    default_propagation_route_table = Column(Boolean, name='default_propagation_route_table', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)