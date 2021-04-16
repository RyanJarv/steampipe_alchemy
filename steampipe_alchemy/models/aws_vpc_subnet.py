from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcSubnet(Base):
    __tablename__ = 'aws_vpc_subnet'
    subnet_id = Column(Text, name='subnet_id', nullable=True)
    subnet_arn = Column(Text, name='subnet_arn', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    cidr_block = Column(psql.CIDR, name='cidr_block', nullable=True)
    state = Column(Text, name='state', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    assign_ipv6_address_on_creation = Column(Boolean, name='assign_ipv6_address_on_creation', nullable=True)
    available_ip_address_count = Column(BigInteger, name='available_ip_address_count', nullable=True)
    availability_zone = Column(Text, name='availability_zone', nullable=True)
    availability_zone_id = Column(Text, name='availability_zone_id', nullable=True)
    customer_owned_ipv4_pool = Column(Text, name='customer_owned_ipv4_pool', nullable=True)
    default_for_az = Column(Boolean, name='default_for_az', nullable=True)
    map_customer_owned_ip_on_launch = Column(Boolean, name='map_customer_owned_ip_on_launch', nullable=True)
    map_public_ip_on_launch = Column(Boolean, name='map_public_ip_on_launch', nullable=True)
    outpost_arn = Column(Text, name='outpost_arn', nullable=True)
    ipv6_cidr_block_association_set = Column(JSON, name='ipv6_cidr_block_association_set', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)