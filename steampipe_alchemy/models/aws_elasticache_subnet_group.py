from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticacheSubnetGroup(Base):
    __tablename__ = 'aws_elasticache_subnet_group'
    cache_subnet_group_name = Column('cache_subnet_group_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cache_subnet_group_description = Column('cache_subnet_group_description', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    subnets = Column('subnets', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)