from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcSubnet(Base):
    __tablename__ = 'aws_vpc_subnet'
    subnet_id = Column('subnet_id', Text, nullable=True)
    subnet_arn = Column('subnet_arn', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    cidr_block = Column('cidr_block', psql.CIDR, nullable=True)
    state = Column('state', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    assign_ipv6_address_on_creation = Column('assign_ipv6_address_on_creation', Boolean, nullable=True)
    available_ip_address_count = Column('available_ip_address_count', BigInteger, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    availability_zone_id = Column('availability_zone_id', Text, nullable=True)
    customer_owned_ipv4_pool = Column('customer_owned_ipv4_pool', Text, nullable=True)
    default_for_az = Column('default_for_az', Boolean, nullable=True)
    map_customer_owned_ip_on_launch = Column('map_customer_owned_ip_on_launch', Boolean, nullable=True)
    map_public_ip_on_launch = Column('map_public_ip_on_launch', Boolean, nullable=True)
    outpost_arn = Column('outpost_arn', Text, nullable=True)
    ipv6_cidr_block_association_set = Column('ipv6_cidr_block_association_set', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)