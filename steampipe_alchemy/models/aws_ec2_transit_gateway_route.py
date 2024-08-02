from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2TransitGatewayRoute(Base, FormatMixins):
    __tablename__ = 'aws_ec2_transit_gateway_route'
    _ctx = Column('_ctx', JSON, nullable=True)
    destination_cidr_block = Column('destination_cidr_block', psql.CIDR, nullable=True)
    transit_gateway_attachments = Column('transit_gateway_attachments', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    transit_gateway_route_table_id = Column('transit_gateway_route_table_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    prefix_list_id = Column('prefix_list_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    type = Column('type', Text, nullable=True)