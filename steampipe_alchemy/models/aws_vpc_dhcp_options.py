from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcDhcpOptions(Base):
    __tablename__ = 'aws_vpc_dhcp_options'
    dhcp_options_id = Column('dhcp_options_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    domain_name = Column('domain_name', JSON, nullable=True)
    domain_name_servers = Column('domain_name_servers', JSON, nullable=True)
    netbios_name_servers = Column('netbios_name_servers', JSON, nullable=True)
    netbios_node_type = Column('netbios_node_type', JSON, nullable=True)
    ntp_servers = Column('ntp_servers', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)