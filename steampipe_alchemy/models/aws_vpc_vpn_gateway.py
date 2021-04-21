from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcVpnGateway(Base):
    __tablename__ = 'aws_vpc_vpn_gateway'
    vpn_gateway_id = Column(name='vpn_gateway_id', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    amazon_side_asn = Column(name='amazon_side_asn', type_=BigInteger, nullable=True)
    availability_zone = Column(name='availability_zone', type_=Text, nullable=True)
    vpc_attachments = Column(name='vpc_attachments', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)