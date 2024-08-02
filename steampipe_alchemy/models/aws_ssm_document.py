from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsmDocument(Base, FormatMixins):
    __tablename__ = 'aws_ssm_document'
    _ctx = Column('_ctx', JSON, nullable=True)
    account_ids = Column('account_ids', JSON, nullable=True)
    account_sharing_info_list = Column('account_sharing_info_list', JSON, nullable=True)
    attachments_information = Column('attachments_information', JSON, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    platform_types = Column('platform_types', JSON, nullable=True)
    requires = Column('requires', JSON, nullable=True)
    review_information = Column('review_information', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    hash = Column('hash', Text, nullable=True)
    hash_type = Column('hash_type', Text, nullable=True)
    latest_version = Column('latest_version', Text, nullable=True)
    owner_type = Column('owner_type', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    pending_review_version = Column('pending_review_version', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    review_status = Column('review_status', Text, nullable=True)
    schema_version = Column('schema_version', Text, nullable=True)
    sha1 = Column('sha1', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    status_information = Column('status_information', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    target_type = Column('target_type', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    approved_version = Column('approved_version', Text, nullable=True)
    version_name = Column('version_name', Text, nullable=True)
    author = Column('author', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    default_version = Column('default_version', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    document_format = Column('document_format', Text, nullable=True)
    document_type = Column('document_type', Text, nullable=True)
    document_version = Column('document_version', Text, nullable=True)