from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpc(Base):
    __tablename__ = 'aws_vpc'
    vpc_id = Column('vpc_id', Text, nullable=True)
    cidr_block = Column('cidr_block', psql.CIDR, nullable=True)
    state = Column('state', Text, nullable=True)
    is_default = Column('is_default', Boolean, nullable=True)
    dhcp_options_id = Column('dhcp_options_id', Text, nullable=True)
    instance_tenancy = Column('instance_tenancy', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    cidr_block_association_set = Column('cidr_block_association_set', JSON, nullable=True)
    ipv6_cidr_block_association_set = Column('ipv6_cidr_block_association_set', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)