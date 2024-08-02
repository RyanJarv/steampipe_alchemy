from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcVpnGateway(Base, FormatMixins):
    __tablename__ = 'aws_vpc_vpn_gateway'
    akas = Column('akas', JSON, nullable=True)
    vpc_attachments = Column('vpc_attachments', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    amazon_side_asn = Column('amazon_side_asn', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    state = Column('state', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    vpn_gateway_id = Column('vpn_gateway_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)