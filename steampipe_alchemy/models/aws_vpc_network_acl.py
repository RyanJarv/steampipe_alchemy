from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcNetworkAcl(Base):
    __tablename__ = 'aws_vpc_network_acl'
    network_acl_id = Column(name='network_acl_id', type_=Text, nullable=True)
    is_default = Column(name='is_default', type_=Boolean, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    associations = Column(name='associations', type_=JSON, nullable=True)
    entries = Column(name='entries', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)