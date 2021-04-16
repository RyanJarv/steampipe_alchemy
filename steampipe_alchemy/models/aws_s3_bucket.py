from sqlalchemy import Column
from sqlalchemy.orm import Query
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsS3Bucket(Base):
    __tablename__ = 'aws_s3_bucket'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    creation_date = Column(TIMESTAMP, name='creation_date', nullable=True)
    bucket_policy_is_public = Column(Boolean, name='bucket_policy_is_public', nullable=True)
    versioning_enabled = Column(Boolean, name='versioning_enabled', nullable=True)
    versioning_mfa_delete = Column(Boolean, name='versioning_mfa_delete', nullable=True)
    block_public_acls = Column(Boolean, name='block_public_acls', nullable=True)
    block_public_policy = Column(Boolean, name='block_public_policy', nullable=True)
    ignore_public_acls = Column(Boolean, name='ignore_public_acls', nullable=True)
    restrict_public_buckets = Column(Boolean, name='restrict_public_buckets', nullable=True)
    server_side_encryption_configuration = Column(JSON, name='server_side_encryption_configuration', nullable=True)
    acl = Column(JSON, name='acl', nullable=True)
    lifecycle_rules = Column(JSON, name='lifecycle_rules', nullable=True)
    logging = Column(JSON, name='logging', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    replication = Column(JSON, name='replication', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    region = Column(Text, name='region', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)
