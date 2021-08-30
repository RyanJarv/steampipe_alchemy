from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudfrontOriginRequestPolicy(Base, FormatMixins):
    __tablename__ = 'aws_cloudfront_origin_request_policy'
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    cookies_config = Column('cookies_config', JSON, nullable=True)
    headers_config = Column('headers_config', JSON, nullable=True)
    query_strings_config = Column('query_strings_config', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    comment = Column('comment', Text, nullable=True)
    etag = Column('etag', Text, nullable=True)
    title = Column('title', Text, nullable=True)