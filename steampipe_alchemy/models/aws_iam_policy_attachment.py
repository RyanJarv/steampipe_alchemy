from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamPolicyAttachment(Base, FormatMixins):
    __tablename__ = 'aws_iam_policy_attachment'
    policy_groups = Column('policy_groups', JSON, nullable=True)
    policy_roles = Column('policy_roles', JSON, nullable=True)
    policy_users = Column('policy_users', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    is_attached = Column('is_attached', Boolean, nullable=True)
    partition = Column('partition', Text, nullable=True)
    policy_arn = Column('policy_arn', Text, nullable=True, primary_key=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
