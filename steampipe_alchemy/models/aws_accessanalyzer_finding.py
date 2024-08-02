from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAccessanalyzerFinding(Base, FormatMixins):
    __tablename__ = 'aws_accessanalyzer_finding'
    _ctx = Column('_ctx', JSON, nullable=True)
    analyzed_at = Column('analyzed_at', TIMESTAMP, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    is_public = Column('is_public', Boolean, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    action = Column('action', JSON, nullable=True)
    sources = Column('sources', JSON, nullable=True)
    principal = Column('principal', JSON, nullable=True)
    condition = Column('condition', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    access_analyzer_arn = Column('access_analyzer_arn', Text, nullable=True)
    error = Column('error', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    resource = Column('resource', Text, nullable=True)
    resource_owner_account = Column('resource_owner_account', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    status = Column('status', Text, nullable=True)