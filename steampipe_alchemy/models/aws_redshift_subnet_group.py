from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRedshiftSubnetGroup(Base):
    __tablename__ = 'aws_redshift_subnet_group'
    cluster_subnet_group_name = Column(name='cluster_subnet_group_name', type_=Text, nullable=True)
    subnet_group_status = Column(name='subnet_group_status', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    subnets = Column(name='subnets', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)