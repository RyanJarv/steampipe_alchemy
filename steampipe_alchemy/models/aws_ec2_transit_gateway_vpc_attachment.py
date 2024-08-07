from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2TransitGatewayVpcAttachment(Base, FormatMixins):
    __tablename__ = 'aws_ec2_transit_gateway_vpc_attachment'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    resource_owner_id = Column('resource_owner_id', Text, nullable=True)
    association_state = Column('association_state', Text, nullable=True)
    association_transit_gateway_route_table_id = Column('association_transit_gateway_route_table_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    transit_gateway_attachment_id = Column('transit_gateway_attachment_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    transit_gateway_id = Column('transit_gateway_id', Text, nullable=True)
    transit_gateway_owner_id = Column('transit_gateway_owner_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)