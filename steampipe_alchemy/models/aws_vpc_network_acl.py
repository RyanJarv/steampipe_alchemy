from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcNetworkAcl(Base):
    __tablename__ = 'aws_vpc_network_acl'
    network_acl_id = Column(Text, name='network_acl_id', nullable=True)
    is_default = Column(Boolean, name='is_default', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    associations = Column(JSON, name='associations', nullable=True)
    entries = Column(JSON, name='entries', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)