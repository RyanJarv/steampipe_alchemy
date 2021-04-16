from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsElasticacheParameterGroup(Base):
    __tablename__ = 'aws_elasticache_parameter_group'
    cache_parameter_group_name = Column(Text, name='cache_parameter_group_name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    description = Column(Text, name='description', nullable=True)
    cache_parameter_group_family = Column(Text, name='cache_parameter_group_family', nullable=True)
    is_global = Column(Boolean, name='is_global', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)