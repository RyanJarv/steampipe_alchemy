from typing import List

from sqlalchemy import Column
from sqlalchemy.orm import Query
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpc(Base):
    query: Query
    __tablename__ = 'aws_vpc'
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    cidr_block = Column(psql.CIDR, name='cidr_block', nullable=True)
    state = Column(Text, name='state', nullable=True)
    is_default = Column(Boolean, name='is_default', nullable=True)
    dhcp_options_id = Column(Text, name='dhcp_options_id', nullable=True)
    instance_tenancy = Column(Text, name='instance_tenancy', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    cidr_block_association_set = Column(JSON, name='cidr_block_association_set', nullable=True)
    ipv6_cidr_block_association_set = Column(JSON, name='ipv6_cidr_block_association_set', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)
