from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcDhcpOptions(Base):
    __tablename__ = 'aws_vpc_dhcp_options'
    dhcp_options_id = Column(Text, name='dhcp_options_id', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    domain_name = Column(JSON, name='domain_name', nullable=True)
    domain_name_servers = Column(JSON, name='domain_name_servers', nullable=True)
    netbios_name_servers = Column(JSON, name='netbios_name_servers', nullable=True)
    netbios_node_type = Column(JSON, name='netbios_node_type', nullable=True)
    ntp_servers = Column(JSON, name='ntp_servers', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)