from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsKmsKey(Base, FormatMixins):
    __tablename__ = 'aws_kms_key'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    enabled = Column('enabled', Boolean, nullable=True)
    deletion_date = Column('deletion_date', TIMESTAMP, nullable=True)
    valid_to = Column('valid_to', TIMESTAMP, nullable=True)
    aliases = Column('aliases', JSON, nullable=True)
    key_rotation_enabled = Column('key_rotation_enabled', Boolean, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    key_manager = Column('key_manager', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    aws_account_id = Column('aws_account_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    customer_master_key_spec = Column('customer_master_key_spec', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    key_state = Column('key_state', Text, nullable=True)
    key_usage = Column('key_usage', Text, nullable=True)
    origin = Column('origin', Text, nullable=True)
    title = Column('title', Text, nullable=True)