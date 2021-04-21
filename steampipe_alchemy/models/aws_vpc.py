from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpc(Base):
    __tablename__ = 'aws_vpc'
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    cidr_block = Column(name='cidr_block', type_=psql.CIDR, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    is_default = Column(name='is_default', type_=Boolean, nullable=True)
    dhcp_options_id = Column(name='dhcp_options_id', type_=Text, nullable=True)
    instance_tenancy = Column(name='instance_tenancy', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    cidr_block_association_set = Column(name='cidr_block_association_set', type_=JSON, nullable=True)
    ipv6_cidr_block_association_set = Column(name='ipv6_cidr_block_association_set', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)