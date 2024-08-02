from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSecurityhubMember(Base, FormatMixins):
    __tablename__ = 'aws_securityhub_member'
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    invited_at = Column('invited_at', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    member_status = Column('member_status', Text, nullable=True)
    member_account_id = Column('member_account_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    administrator_id = Column('administrator_id', Text, nullable=True)
    email = Column('email', Text, nullable=True)
    master_id = Column('master_id', Text, nullable=True)