from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamGroup(Base):
    __tablename__ = 'aws_iam_group'
    name = Column(name='name', type_=Text, nullable=True)
    group_id = Column(name='group_id', type_=Text, nullable=True)
    path = Column(name='path', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    create_date = Column(name='create_date', type_=TIMESTAMP, nullable=True)
    inline_policies = Column(name='inline_policies', type_=JSON, nullable=True)
    inline_policies_std = Column(name='inline_policies_std', type_=JSON, nullable=True)
    attached_policy_arns = Column(name='attached_policy_arns', type_=JSON, nullable=True)
    users = Column(name='users', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)