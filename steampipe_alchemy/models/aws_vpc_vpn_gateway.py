from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcVpnGateway(Base):
    __tablename__ = 'aws_vpc_vpn_gateway'
    vpn_gateway_id = Column(Text, name='vpn_gateway_id', nullable=True)
    state = Column(Text, name='state', nullable=True)
    type = Column(Text, name='type', nullable=True)
    amazon_side_asn = Column(BigInteger, name='amazon_side_asn', nullable=True)
    availability_zone = Column(Text, name='availability_zone', nullable=True)
    vpc_attachments = Column(JSON, name='vpc_attachments', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)