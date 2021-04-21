from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcEip(Base):
    __tablename__ = 'aws_vpc_eip'
    allocation_id = Column(name='allocation_id', type_=Text, nullable=True)
    public_ip = Column(name='public_ip', type_=psql.INET, nullable=True)
    public_ipv4_pool = Column(name='public_ipv4_pool', type_=Text, nullable=True)
    domain = Column(name='domain', type_=Text, nullable=True)
    association_id = Column(name='association_id', type_=Text, nullable=True)
    carrier_ip = Column(name='carrier_ip', type_=Text, nullable=True)
    customer_owned_ip = Column(name='customer_owned_ip', type_=psql.INET, nullable=True)
    customer_owned_ipv4_pool = Column(name='customer_owned_ipv4_pool', type_=Text, nullable=True)
    instance_id = Column(name='instance_id', type_=Text, nullable=True)
    network_border_group = Column(name='network_border_group', type_=Text, nullable=True)
    network_interface_id = Column(name='network_interface_id', type_=Text, nullable=True)
    network_interface_owner_id = Column(name='network_interface_owner_id', type_=Text, nullable=True)
    private_ip_address = Column(name='private_ip_address', type_=psql.INET, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)