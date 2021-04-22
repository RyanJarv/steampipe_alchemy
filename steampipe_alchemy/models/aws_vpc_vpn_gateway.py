from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcVpnGateway(Base):
    __tablename__ = 'aws_vpc_vpn_gateway'
    vpn_gateway_id = Column('vpn_gateway_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    amazon_side_asn = Column('amazon_side_asn', BigInteger, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    vpc_attachments = Column('vpc_attachments', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)