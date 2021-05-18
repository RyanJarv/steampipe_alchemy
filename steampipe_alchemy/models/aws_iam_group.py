from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsIamGroup(Base, FormatMixins):
    __tablename__ = 'aws_iam_group'
    name = Column('name', Text, nullable=True)
    group_id = Column('group_id', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    inline_policies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    users = Column('users', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsIamGroupLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_iam_group_local'
    name = Column('name', Text, nullable=True)
    group_id = Column('group_id', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    inline_policies = Column('inline_policies', JSON, nullable=True)
    inline_policies_std = Column('inline_policies_std', JSON, nullable=True)
    attached_policy_arns = Column('attached_policy_arns', JSON, nullable=True)
    users = Column('users', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsIamGroup).select_from(AwsIamGroup)
create_materialized_view('aws_iam_group_local', cache, db.metadata_materialized)
