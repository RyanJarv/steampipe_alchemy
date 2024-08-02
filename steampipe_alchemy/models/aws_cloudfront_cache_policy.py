from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudfrontCachePolicy(Base, FormatMixins):
    __tablename__ = 'aws_cloudfront_cache_policy'
    _ctx = Column('_ctx', JSON, nullable=True)
    default_ttl = Column('default_ttl', BigInteger, nullable=True)
    max_ttl = Column('max_ttl', BigInteger, nullable=True)
    min_ttl = Column('min_ttl', BigInteger, nullable=True)
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    parameters_in_cache_key_and_forwarded_to_origin = Column('parameters_in_cache_key_and_forwarded_to_origin', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    comment = Column('comment', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    etag = Column('etag', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)