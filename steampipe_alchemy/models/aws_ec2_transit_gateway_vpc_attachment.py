from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2TransitGatewayVpcAttachment(Base):
    __tablename__ = 'aws_ec2_transit_gateway_vpc_attachment'
    transit_gateway_attachment_id = Column(Text, name='transit_gateway_attachment_id', nullable=True)
    transit_gateway_id = Column(Text, name='transit_gateway_id', nullable=True)
    transit_gateway_owner_id = Column(Text, name='transit_gateway_owner_id', nullable=True)
    state = Column(Text, name='state', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    resource_id = Column(Text, name='resource_id', nullable=True)
    resource_type = Column(Text, name='resource_type', nullable=True)
    resource_owner_id = Column(Text, name='resource_owner_id', nullable=True)
    association_state = Column(Text, name='association_state', nullable=True)
    association_transit_gateway_route_table_id = Column(Text, name='association_transit_gateway_route_table_id', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)