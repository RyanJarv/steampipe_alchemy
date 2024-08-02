from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodeartifactDomain(Base, FormatMixins):
    __tablename__ = 'aws_codeartifact_domain'
    _ctx = Column('_ctx', JSON, nullable=True)
    asset_size_bytes = Column('asset_size_bytes', BigInteger, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    repository_count = Column('repository_count', BigInteger, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    encryption_key = Column('encryption_key', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    s3_bucket_arn = Column('s3_bucket_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)