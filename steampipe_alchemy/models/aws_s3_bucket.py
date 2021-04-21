from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsS3Bucket(Base):
    __tablename__ = 'aws_s3_bucket'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    creation_date = Column(name='creation_date', type_=TIMESTAMP, nullable=True)
    bucket_policy_is_public = Column(name='bucket_policy_is_public', type_=Boolean, nullable=True)
    versioning_enabled = Column(name='versioning_enabled', type_=Boolean, nullable=True)
    versioning_mfa_delete = Column(name='versioning_mfa_delete', type_=Boolean, nullable=True)
    block_public_acls = Column(name='block_public_acls', type_=Boolean, nullable=True)
    block_public_policy = Column(name='block_public_policy', type_=Boolean, nullable=True)
    ignore_public_acls = Column(name='ignore_public_acls', type_=Boolean, nullable=True)
    restrict_public_buckets = Column(name='restrict_public_buckets', type_=Boolean, nullable=True)
    server_side_encryption_configuration = Column(name='server_side_encryption_configuration', type_=JSON, nullable=True)
    acl = Column(name='acl', type_=JSON, nullable=True)
    lifecycle_rules = Column(name='lifecycle_rules', type_=JSON, nullable=True)
    logging = Column(name='logging', type_=JSON, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    replication = Column(name='replication', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)