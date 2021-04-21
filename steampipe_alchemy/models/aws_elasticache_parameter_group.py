from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticacheParameterGroup(Base):
    __tablename__ = 'aws_elasticache_parameter_group'
    cache_parameter_group_name = Column(name='cache_parameter_group_name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    cache_parameter_group_family = Column(name='cache_parameter_group_family', type_=Text, nullable=True)
    is_global = Column(name='is_global', type_=Boolean, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)