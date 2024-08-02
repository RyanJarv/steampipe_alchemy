from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsmDocumentPermission(Base, FormatMixins):
    __tablename__ = 'aws_ssm_document_permission'
    account_ids = Column('account_ids', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    document_name = Column('document_name', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    shared_account_id = Column('shared_account_id', Text, nullable=True)
    shared_document_version = Column('shared_document_version', Text, nullable=True)