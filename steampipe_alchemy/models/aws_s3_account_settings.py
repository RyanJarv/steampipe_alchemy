from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsS3AccountSettings(Base, FormatMixins):
    __tablename__ = 'aws_s3_account_settings'
    akas = Column('akas', JSON, nullable=True)
    ignore_public_acls = Column('ignore_public_acls', Boolean, nullable=True)
    restrict_public_buckets = Column('restrict_public_buckets', Boolean, nullable=True)
    block_public_acls = Column('block_public_acls', Boolean, nullable=True)
    block_public_policy = Column('block_public_policy', Boolean, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)