from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcDhcpOptions(Base):
    __tablename__ = 'aws_vpc_dhcp_options'
    dhcp_options_id = Column(name='dhcp_options_id', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    domain_name = Column(name='domain_name', type_=JSON, nullable=True)
    domain_name_servers = Column(name='domain_name_servers', type_=JSON, nullable=True)
    netbios_name_servers = Column(name='netbios_name_servers', type_=JSON, nullable=True)
    netbios_node_type = Column(name='netbios_node_type', type_=JSON, nullable=True)
    ntp_servers = Column(name='ntp_servers', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)