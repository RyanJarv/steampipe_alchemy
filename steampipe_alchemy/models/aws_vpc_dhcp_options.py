from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcDhcpOptions(Base, FormatMixins):
    __tablename__ = 'aws_vpc_dhcp_options'
    akas = Column('akas', JSON, nullable=True)
    domain_name_servers = Column('domain_name_servers', JSON, nullable=True)
    netbios_name_servers = Column('netbios_name_servers', JSON, nullable=True)
    netbios_node_type = Column('netbios_node_type', JSON, nullable=True)
    ntp_servers = Column('ntp_servers', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    domain_name = Column('domain_name', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    dhcp_options_id = Column('dhcp_options_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)