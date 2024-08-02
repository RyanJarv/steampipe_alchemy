from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsTrustedAdvisorCheckSummary(Base, FormatMixins):
    __tablename__ = 'aws_trusted_advisor_check_summary'
    _ctx = Column('_ctx', JSON, nullable=True)
    timestamp = Column('timestamp', TIMESTAMP, nullable=True)
    resources_flagged = Column('resources_flagged', BigInteger, nullable=True)
    resources_ignored = Column('resources_ignored', BigInteger, nullable=True)
    resources_processed = Column('resources_processed', BigInteger, nullable=True)
    resources_suppressed = Column('resources_suppressed', BigInteger, nullable=True)
    category_specific_summary = Column('category_specific_summary', JSON, nullable=True)
    _metadata = Column('_metadata', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    check_id = Column('check_id', Text, nullable=True)
    category = Column('category', Text, nullable=True)
    language = Column('language', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
