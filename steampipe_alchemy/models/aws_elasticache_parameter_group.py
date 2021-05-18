from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsElasticacheParameterGroup(Base, FormatMixins):
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


# Local materialized view table
class AwsElasticacheParameterGroupLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_elasticache_parameter_group_local'
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


cache = select(AwsElasticacheParameterGroup).select_from(AwsElasticacheParameterGroup)
create_materialized_view('aws_elasticache_parameter_group_local', cache, db.metadata_materialized)
