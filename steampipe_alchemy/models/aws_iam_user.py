from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamUser(Base):
    __tablename__ = 'aws_iam_user'
    name = Column(name='name', type_=Text, nullable=True)
    user_id = Column(name='user_id', type_=Text, nullable=True)
    path = Column(name='path', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    create_date = Column(name='create_date', type_=TIMESTAMP, nullable=True)
    password_last_used = Column(name='password_last_used', type_=TIMESTAMP, nullable=True)
    permissions_boundary_arn = Column(name='permissions_boundary_arn', type_=Text, nullable=True)
    permissions_boundary_type = Column(name='permissions_boundary_type', type_=Text, nullable=True)
    mfa_enabled = Column(name='mfa_enabled', type_=Boolean, nullable=True)
    mfa_devices = Column(name='mfa_devices', type_=JSON, nullable=True)
    groups = Column(name='groups', type_=JSON, nullable=True)
    inline_policies = Column(name='inline_policies', type_=JSON, nullable=True)
    inline_policies_std = Column(name='inline_policies_std', type_=JSON, nullable=True)
    attached_policy_arns = Column(name='attached_policy_arns', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)