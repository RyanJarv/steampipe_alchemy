from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamRole(Base):
    __tablename__ = 'aws_iam_role'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    role_id = Column(name='role_id', type_=Text, nullable=True)
    create_date = Column(name='create_date', type_=TIMESTAMP, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    instance_profile_arns = Column(name='instance_profile_arns', type_=JSON, nullable=True)
    max_session_duration = Column(name='max_session_duration', type_=BigInteger, nullable=True)
    path = Column(name='path', type_=Text, nullable=True)
    permissions_boundary_arn = Column(name='permissions_boundary_arn', type_=Text, nullable=True)
    permissions_boundary_type = Column(name='permissions_boundary_type', type_=Text, nullable=True)
    role_last_used_date = Column(name='role_last_used_date', type_=TIMESTAMP, nullable=True)
    role_last_used_region = Column(name='role_last_used_region', type_=Text, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    inline_policies = Column(name='inline_policies', type_=JSON, nullable=True)
    inline_policies_std = Column(name='inline_policies_std', type_=JSON, nullable=True)
    attached_policy_arns = Column(name='attached_policy_arns', type_=JSON, nullable=True)
    assume_role_policy = Column(name='assume_role_policy', type_=JSON, nullable=True)
    assume_role_policy_std = Column(name='assume_role_policy_std', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)