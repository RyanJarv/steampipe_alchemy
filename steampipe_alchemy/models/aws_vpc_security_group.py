from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcSecurityGroup(Base):
    __tablename__ = 'aws_vpc_security_group'
    group_name = Column(Text, name='group_name', nullable=True)
    group_id = Column(Text, name='group_id', nullable=True)
    description = Column(Text, name='description', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    ip_permissions = Column(JSON, name='ip_permissions', nullable=True)
    ip_permissions_egress = Column(JSON, name='ip_permissions_egress', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)