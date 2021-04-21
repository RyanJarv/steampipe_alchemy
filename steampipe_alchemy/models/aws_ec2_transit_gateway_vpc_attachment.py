from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2TransitGatewayVpcAttachment(Base):
    __tablename__ = 'aws_ec2_transit_gateway_vpc_attachment'
    transit_gateway_attachment_id = Column(name='transit_gateway_attachment_id', type_=Text, nullable=True)
    transit_gateway_id = Column(name='transit_gateway_id', type_=Text, nullable=True)
    transit_gateway_owner_id = Column(name='transit_gateway_owner_id', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    resource_id = Column(name='resource_id', type_=Text, nullable=True)
    resource_type = Column(name='resource_type', type_=Text, nullable=True)
    resource_owner_id = Column(name='resource_owner_id', type_=Text, nullable=True)
    association_state = Column(name='association_state', type_=Text, nullable=True)
    association_transit_gateway_route_table_id = Column(name='association_transit_gateway_route_table_id', type_=Text, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)