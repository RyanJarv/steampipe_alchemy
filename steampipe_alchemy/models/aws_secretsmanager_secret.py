from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSecretsmanagerSecret(Base, FormatMixins):
    __tablename__ = 'aws_secretsmanager_secret'
    _ctx = Column('_ctx', JSON, nullable=True)
    last_changed_date = Column('last_changed_date', TIMESTAMP, nullable=True)
    last_rotated_date = Column('last_rotated_date', TIMESTAMP, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    replication_status = Column('replication_status', JSON, nullable=True)
    rotation_enabled = Column('rotation_enabled', Boolean, nullable=True)
    rotation_rules = Column('rotation_rules', JSON, nullable=True)
    secret_versions_to_stages = Column('secret_versions_to_stages', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    deleted_date = Column('deleted_date', TIMESTAMP, nullable=True)
    last_accessed_date = Column('last_accessed_date', TIMESTAMP, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    rotation_lambda_arn = Column('rotation_lambda_arn', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    owning_service = Column('owning_service', Text, nullable=True)
    primary_region = Column('primary_region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)