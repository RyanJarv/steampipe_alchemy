from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcVpnConnection(Base, FormatMixins):
    __tablename__ = 'aws_vpc_vpn_connection'
    _ctx = Column('_ctx', JSON, nullable=True)
    options = Column('options', JSON, nullable=True)
    routes = Column('routes', JSON, nullable=True)
    vgw_telemetry = Column('vgw_telemetry', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    transit_gateway_id = Column('transit_gateway_id', Text, nullable=True)
    vpn_connection_id = Column('vpn_connection_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    state = Column('state', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    category = Column('category', Text, nullable=True)
    vpn_gateway_id = Column('vpn_gateway_id', Text, nullable=True)
    customer_gateway_id = Column('customer_gateway_id', Text, nullable=True)
    customer_gateway_configuration = Column('customer_gateway_configuration', Text, nullable=True)