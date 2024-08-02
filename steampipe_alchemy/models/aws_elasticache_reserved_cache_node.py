from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsElasticacheReservedCacheNode(Base, FormatMixins):
    __tablename__ = 'aws_elasticache_reserved_cache_node'
    _ctx = Column('_ctx', JSON, nullable=True)
    cache_node_count = Column('cache_node_count', BigInteger, nullable=True)
    duration = Column('duration', BigInteger, nullable=True)
    fixed_price = Column('fixed_price', psql.DOUBLE_PRECISION, nullable=True)
    start_time = Column('start_time', TIMESTAMP, nullable=True)
    usage_price = Column('usage_price', psql.DOUBLE_PRECISION, nullable=True)
    recurring_charges = Column('recurring_charges', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    product_description = Column('product_description', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    reserved_cache_nodes_offering_id = Column('reserved_cache_nodes_offering_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    cache_node_type = Column('cache_node_type', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    reserved_cache_node_id = Column('reserved_cache_node_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    offering_type = Column('offering_type', Text, nullable=True)