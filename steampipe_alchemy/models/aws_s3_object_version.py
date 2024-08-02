from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsS3ObjectVersion(Base, FormatMixins):
    __tablename__ = 'aws_s3_object_version'
    _ctx = Column('_ctx', JSON, nullable=True)
    size = Column('size', BigInteger, nullable=True)
    is_latest = Column('is_latest', Boolean, nullable=True)
    last_modified = Column('last_modified', TIMESTAMP, nullable=True)
    checksum_algorithm = Column('checksum_algorithm', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    etag = Column('etag', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    bucket_name = Column('bucket_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    region = Column('region', Text, nullable=True)
    key = Column('key', Text, nullable=True)
    storage_class = Column('storage_class', Text, nullable=True)
    version_id = Column('version_id', Text, nullable=True)
    owner_display_name = Column('owner_display_name', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)