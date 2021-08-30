from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamGroup(Base, FormatMixins):
    __tablename__ = 'aws_iam_group'
    users = Column('users', JSON, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    inline_policies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    group_id = Column('group_id', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)