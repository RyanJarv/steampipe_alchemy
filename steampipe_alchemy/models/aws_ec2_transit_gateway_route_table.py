from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2TransitGatewayRouteTable(Base, FormatMixins):
    __tablename__ = 'aws_ec2_transit_gateway_route_table'
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    default_association_route_table = Column('default_association_route_table', Boolean, nullable=True)
    default_propagation_route_table = Column('default_propagation_route_table', Boolean, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    transit_gateway_id = Column('transit_gateway_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    transit_gateway_route_table_id = Column('transit_gateway_route_table_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)