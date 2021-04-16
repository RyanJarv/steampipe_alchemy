from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamUser(Base):
    __tablename__ = 'aws_iam_user'
    name = Column(Text, name='name', nullable=True)
    user_id = Column(Text, name='user_id', nullable=True)
    path = Column(Text, name='path', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    create_date = Column(TIMESTAMP, name='create_date', nullable=True)
    password_last_used = Column(TIMESTAMP, name='password_last_used', nullable=True)
    permissions_boundary_arn = Column(Text, name='permissions_boundary_arn', nullable=True)
    permissions_boundary_type = Column(Text, name='permissions_boundary_type', nullable=True)
    mfa_enabled = Column(Boolean, name='mfa_enabled', nullable=True)
    mfa_devices = Column(JSON, name='mfa_devices', nullable=True)
    groups = Column(JSON, name='groups', nullable=True)
    inline_policies = Column(JSON, name='inline_policies', nullable=True)
    inline_policies_std = Column(JSON, name='inline_policies_std', nullable=True)
    attached_policy_arns = Column(JSON, name='attached_policy_arns', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)