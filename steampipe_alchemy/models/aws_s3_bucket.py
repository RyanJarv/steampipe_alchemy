from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsS3Bucket(Base):
    __tablename__ = 'aws_s3_bucket'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    bucket_policy_is_public = Column('bucket_policy_is_public', Boolean, nullable=True)
    versioning_enabled = Column('versioning_enabled', Boolean, nullable=True)
    versioning_mfa_delete = Column('versioning_mfa_delete', Boolean, nullable=True)
    block_public_acls = Column('block_public_acls', Boolean, nullable=True)
    block_public_policy = Column('block_public_policy', Boolean, nullable=True)
    ignore_public_acls = Column('ignore_public_acls', Boolean, nullable=True)
    restrict_public_buckets = Column('restrict_public_buckets', Boolean, nullable=True)
    server_side_encryption_configuration = Column('server_side_encryption_configuration', JSON, nullable=True)
    acl = Column('acl', JSON, nullable=True)
    lifecycle_rules = Column('lifecycle_rules', JSON, nullable=True)
    logging = Column('logging', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    replication = Column('replication', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)