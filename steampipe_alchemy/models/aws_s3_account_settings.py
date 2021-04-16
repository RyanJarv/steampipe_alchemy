from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsS3AccountSettings(Base):
    __tablename__ = 'aws_s3_account_settings'
    block_public_acls = Column(Boolean, name='block_public_acls', nullable=True)
    block_public_policy = Column(Boolean, name='block_public_policy', nullable=True)
    ignore_public_acls = Column(Boolean, name='ignore_public_acls', nullable=True)
    restrict_public_buckets = Column(Boolean, name='restrict_public_buckets', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)