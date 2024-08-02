from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsInspector2Member(Base, FormatMixins):
    __tablename__ = 'aws_inspector2_member'
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    relationship_status = Column('relationship_status', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    member_account_id = Column('member_account_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    delegated_admin_account_id = Column('delegated_admin_account_id', Text, nullable=True)
    only_associated = Column('only_associated', Text, nullable=True)