from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamRole(Base, FormatMixins):
    __tablename__ = 'aws_iam_role'
    _ctx = Column('_ctx', JSON, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    instance_profile_arns = Column('instance_profile_arns', JSON, nullable=True)
    max_session_duration = Column('max_session_duration', BigInteger, nullable=True)
    role_last_used_date = Column('role_last_used_date', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    inline_policies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    assume_role_policy = Column('assume_role_policy', JSON, nullable=True)
    assume_role_policy_std = Column('assume_role_policy_std', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    role_id = Column('role_id', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    permissions_boundary_arn = Column('permissions_boundary_arn', Text, nullable=True)
    permissions_boundary_type = Column('permissions_boundary_type', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    role_last_used_region = Column('role_last_used_region', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)