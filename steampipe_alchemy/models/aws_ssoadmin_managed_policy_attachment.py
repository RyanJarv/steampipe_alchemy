from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsoadminManagedPolicyAttachment(Base, FormatMixins):
    __tablename__ = 'aws_ssoadmin_managed_policy_attachment'
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    instance_arn = Column('instance_arn', Text, nullable=True)
    managed_policy_arn = Column('managed_policy_arn', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    permission_set_arn = Column('permission_set_arn', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)