from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamRole(Base):
    __tablename__ = 'aws_iam_role'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    role_id = Column('role_id', Text, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    description = Column('description', Text, nullable=True)
    instance_profile_arns = Column('instance_profile_arns', JSON, nullable=True)
    max_session_duration = Column('max_session_duration', BigInteger, nullable=True)
    path = Column('path', Text, nullable=True)
    permissions_boundary_arn = Column('permissions_boundary_arn', Text, nullable=True)
    permissions_boundary_type = Column('permissions_boundary_type', Text, nullable=True)
    role_last_used_date = Column('role_last_used_date', TIMESTAMP, nullable=True)
    role_last_used_region = Column('role_last_used_region', Text, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    inline_policies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    assume_role_policy = Column('assume_role_policy', JSON, nullable=True)
    assume_role_policy_std = Column('assume_role_policy_std', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)