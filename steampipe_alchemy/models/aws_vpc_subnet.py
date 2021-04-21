from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcSubnet(Base):
    __tablename__ = 'aws_vpc_subnet'
    subnet_id = Column(name='subnet_id', type_=Text, nullable=True)
    subnet_arn = Column(name='subnet_arn', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    cidr_block = Column(name='cidr_block', type_=psql.CIDR, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    assign_ipv6_address_on_creation = Column(name='assign_ipv6_address_on_creation', type_=Boolean, nullable=True)
    available_ip_address_count = Column(name='available_ip_address_count', type_=BigInteger, nullable=True)
    availability_zone = Column(name='availability_zone', type_=Text, nullable=True)
    availability_zone_id = Column(name='availability_zone_id', type_=Text, nullable=True)
    customer_owned_ipv4_pool = Column(name='customer_owned_ipv4_pool', type_=Text, nullable=True)
    default_for_az = Column(name='default_for_az', type_=Boolean, nullable=True)
    map_customer_owned_ip_on_launch = Column(name='map_customer_owned_ip_on_launch', type_=Boolean, nullable=True)
    map_public_ip_on_launch = Column(name='map_public_ip_on_launch', type_=Boolean, nullable=True)
    outpost_arn = Column(name='outpost_arn', type_=Text, nullable=True)
    ipv6_cidr_block_association_set = Column(name='ipv6_cidr_block_association_set', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)