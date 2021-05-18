from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsS3AccountSettings(Base, FormatMixins):
    __tablename__ = 'aws_s3_account_settings'
    block_public_acls = Column('block_public_acls', Boolean, nullable=True)
    block_public_policy = Column('block_public_policy', Boolean, nullable=True)
    ignore_public_acls = Column('ignore_public_acls', Boolean, nullable=True)
    restrict_public_buckets = Column('restrict_public_buckets', Boolean, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsS3AccountSettingsLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_s3_account_settings_local'
    block_public_acls = Column('block_public_acls', Boolean, nullable=True)
    block_public_policy = Column('block_public_policy', Boolean, nullable=True)
    ignore_public_acls = Column('ignore_public_acls', Boolean, nullable=True)
    restrict_public_buckets = Column('restrict_public_buckets', Boolean, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsS3AccountSettings).select_from(AwsS3AccountSettings)
create_materialized_view('aws_s3_account_settings_local', cache, db.metadata_materialized)
