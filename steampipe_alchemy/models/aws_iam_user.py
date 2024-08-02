from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamUser(Base, FormatMixins):
    __tablename__ = 'aws_iam_user'
    _ctx = Column('_ctx', JSON, nullable=True)
    mfa_enabled = Column('mfa_enabled', Boolean, nullable=True)
    login_profile = Column('login_profile', JSON, nullable=True)
    mfa_devices = Column('mfa_devices', JSON, nullable=True)
    groups = Column('groups', JSON, nullable=True)
    inline_policies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    password_last_used = Column('password_last_used', TIMESTAMP, nullable=True)
    user_id = Column('user_id', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    permissions_boundary_arn = Column('permissions_boundary_arn', Text, nullable=True)
    permissions_boundary_type = Column('permissions_boundary_type', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)