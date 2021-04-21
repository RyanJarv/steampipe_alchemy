from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsS3AccountSettings(Base):
    __tablename__ = 'aws_s3_account_settings'
    block_public_acls = Column(name='block_public_acls', type_=Boolean, nullable=True)
    block_public_policy = Column(name='block_public_policy', type_=Boolean, nullable=True)
    ignore_public_acls = Column(name='ignore_public_acls', type_=Boolean, nullable=True)
    restrict_public_buckets = Column(name='restrict_public_buckets', type_=Boolean, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)