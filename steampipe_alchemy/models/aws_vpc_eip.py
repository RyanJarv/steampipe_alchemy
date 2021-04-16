from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcEip(Base):
    __tablename__ = 'aws_vpc_eip'
    allocation_id = Column(Text, name='allocation_id', nullable=True)
    public_ip = Column(psql.INET, name='public_ip', nullable=True)
    public_ipv4_pool = Column(Text, name='public_ipv4_pool', nullable=True)
    domain = Column(Text, name='domain', nullable=True)
    association_id = Column(Text, name='association_id', nullable=True)
    carrier_ip = Column(Text, name='carrier_ip', nullable=True)
    customer_owned_ip = Column(psql.INET, name='customer_owned_ip', nullable=True)
    customer_owned_ipv4_pool = Column(Text, name='customer_owned_ipv4_pool', nullable=True)
    instance_id = Column(Text, name='instance_id', nullable=True)
    network_border_group = Column(Text, name='network_border_group', nullable=True)
    network_interface_id = Column(Text, name='network_interface_id', nullable=True)
    network_interface_owner_id = Column(Text, name='network_interface_owner_id', nullable=True)
    private_ip_address = Column(psql.INET, name='private_ip_address', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)