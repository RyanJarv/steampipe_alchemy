from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudfrontOriginRequestPolicy(Base, FormatMixins):
    __tablename__ = 'aws_cloudfront_origin_request_policy'
    akas = Column('akas', JSON, nullable=True)
    cookies_config = Column('cookies_config', JSON, nullable=True)
    headers_config = Column('headers_config', JSON, nullable=True)
    query_strings_config = Column('query_strings_config', JSON, nullable=True)
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    comment = Column('comment', Text, nullable=True)
    etag = Column('etag', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)