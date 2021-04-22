from typing import List

from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP

from steampipe_alchemy import Base
from steampipe_alchemy.types.policy import Policy


class AwsIamUser(Base):
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
    inline_policies_std: List[Policy] = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)