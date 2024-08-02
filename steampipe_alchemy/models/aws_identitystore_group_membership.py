from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIdentitystoreGroupMembership(Base, FormatMixins):
    __tablename__ = 'aws_identitystore_group_membership'
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    group_id = Column('group_id', Text, nullable=True)
    member_id = Column('member_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    membership_id = Column('membership_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    identity_store_id = Column('identity_store_id', Text, nullable=True)