from steampipe_alchemy.types.aws_iam_user import *

from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

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
    mfa_devices: MfaDevices = Column('mfa_devices', JSON, nullable=True)
    groups: Groups = Column('groups', JSON, nullable=True)
    inline_policies: InlinePolicies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std: InlinePoliciesStd = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns: AttachedPolicyArns = Column('attached_policy_arns', JSON, nullable=True)
    tags_src: TagsSrc = Column('tags_src', JSON, nullable=True)
    tags: Tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas: Akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)