from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcSecurityGroup(Base):
    __tablename__ = 'aws_vpc_security_group'
    group_name = Column(name='group_name', type_=Text, nullable=True)
    group_id = Column(name='group_id', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    ip_permissions = Column(name='ip_permissions', type_=JSON, nullable=True)
    ip_permissions_egress = Column(name='ip_permissions_egress', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)