from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsIamUser(Base, FormatMixins):
    __tablename__ = 'aws_iam_user'
    name = Column('name', Text, nullable=True)
    user_id = Column('user_id', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    password_last_used = Column('password_last_used', TIMESTAMP, nullable=True)
    permissions_boundary_arn = Column('permissions_boundary_arn', Text, nullable=True)
    permissions_boundary_type = Column('permissions_boundary_type', Text, nullable=True)
    mfa_enabled = Column('mfa_enabled', Boolean, nullable=True)
    mfa_devices = Column('mfa_devices', JSON, nullable=True)
    groups = Column('groups', JSON, nullable=True)
    inline_policies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsIamUserLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_iam_user_local'
    name = Column('name', Text, nullable=True)
    user_id = Column('user_id', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    password_last_used = Column('password_last_used', TIMESTAMP, nullable=True)
    permissions_boundary_arn = Column('permissions_boundary_arn', Text, nullable=True)
    permissions_boundary_type = Column('permissions_boundary_type', Text, nullable=True)
    mfa_enabled = Column('mfa_enabled', Boolean, nullable=True)
    mfa_devices = Column('mfa_devices', JSON, nullable=True)
    groups = Column('groups', JSON, nullable=True)
    inline_policies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsIamUser).select_from(AwsIamUser)
create_materialized_view('aws_iam_user_local', cache, db.metadata_materialized)
