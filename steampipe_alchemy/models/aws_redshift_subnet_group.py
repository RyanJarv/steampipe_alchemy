from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRedshiftSubnetGroup(Base):
    __tablename__ = 'aws_redshift_subnet_group'
    cluster_subnet_group_name = Column(Text, name='cluster_subnet_group_name', nullable=True)
    subnet_group_status = Column(Text, name='subnet_group_status', nullable=True)
    description = Column(Text, name='description', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    subnets = Column(JSON, name='subnets', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)