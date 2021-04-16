from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamRole(Base):
    __tablename__ = 'aws_iam_role'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    role_id = Column(Text, name='role_id', nullable=True)
    create_date = Column(TIMESTAMP, name='create_date', nullable=True)
    description = Column(Text, name='description', nullable=True)
    instance_profile_arns = Column(JSON, name='instance_profile_arns', nullable=True)
    max_session_duration = Column(BigInteger, name='max_session_duration', nullable=True)
    path = Column(Text, name='path', nullable=True)
    permissions_boundary_arn = Column(Text, name='permissions_boundary_arn', nullable=True)
    permissions_boundary_type = Column(Text, name='permissions_boundary_type', nullable=True)
    role_last_used_date = Column(TIMESTAMP, name='role_last_used_date', nullable=True)
    role_last_used_region = Column(Text, name='role_last_used_region', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    inline_policies = Column(JSON, name='inline_policies', nullable=True)
    inline_policies_std = Column(JSON, name='inline_policies_std', nullable=True)
    attached_policy_arns = Column(JSON, name='attached_policy_arns', nullable=True)
    assume_role_policy = Column(JSON, name='assume_role_policy', nullable=True)
    assume_role_policy_std = Column(JSON, name='assume_role_policy_std', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)