from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsEc2TransitGatewayRouteTable(Base, FormatMixins):
    __tablename__ = 'aws_ec2_transit_gateway_route_table'
    transit_gateway_route_table_id = Column('transit_gateway_route_table_id', Text, nullable=True)
    transit_gateway_id = Column('transit_gateway_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    default_association_route_table = Column('default_association_route_table', Boolean, nullable=True)
    default_propagation_route_table = Column('default_propagation_route_table', Boolean, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsEc2TransitGatewayRouteTableLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_ec2_transit_gateway_route_table_local'
    transit_gateway_route_table_id = Column('transit_gateway_route_table_id', Text, nullable=True)
    transit_gateway_id = Column('transit_gateway_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    default_association_route_table = Column('default_association_route_table', Boolean, nullable=True)
    default_propagation_route_table = Column('default_propagation_route_table', Boolean, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsEc2TransitGatewayRouteTable).select_from(AwsEc2TransitGatewayRouteTable)
create_materialized_view('aws_ec2_transit_gateway_route_table_local', cache, db.metadata_materialized)
