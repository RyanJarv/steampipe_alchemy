from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudfrontOriginAccessIdentity(Base, FormatMixins):
    __tablename__ = 'aws_cloudfront_origin_access_identity'
    akas = Column('akas', JSON, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    s3_canonical_user_id = Column('s3_canonical_user_id', Text, nullable=True)
    caller_reference = Column('caller_reference', Text, nullable=True)
    comment = Column('comment', Text, nullable=True)
    etag = Column('etag', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)