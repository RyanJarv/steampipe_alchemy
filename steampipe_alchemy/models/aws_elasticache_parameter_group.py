from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticacheParameterGroup(Base):
    __tablename__ = 'aws_elasticache_parameter_group'
    cache_parameter_group_name = Column('cache_parameter_group_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    cache_parameter_group_family = Column('cache_parameter_group_family', Text, nullable=True)
    is_global = Column('is_global', Boolean, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
