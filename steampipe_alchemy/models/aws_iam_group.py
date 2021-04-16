from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamGroup(Base):
    __tablename__ = 'aws_iam_group'
    name = Column(Text, name='name', nullable=True)
    group_id = Column(Text, name='group_id', nullable=True)
    path = Column(Text, name='path', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    create_date = Column(TIMESTAMP, name='create_date', nullable=True)
    inline_policies = Column(JSON, name='inline_policies', nullable=True)
    inline_policies_std = Column(JSON, name='inline_policies_std', nullable=True)
    attached_policy_arns = Column(JSON, name='attached_policy_arns', nullable=True)
    users = Column(JSON, name='users', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)