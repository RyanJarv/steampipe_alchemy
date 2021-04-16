from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSsmDocument(Base):
    __tablename__ = 'aws_ssm_document'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    account_ids = Column(JSON, name='account_ids', nullable=True)
    account_sharing_info_list = Column(JSON, name='account_sharing_info_list', nullable=True)
    approved_version = Column(Text, name='approved_version', nullable=True)
    attachments_information = Column(JSON, name='attachments_information', nullable=True)
    author = Column(Text, name='author', nullable=True)
    created_date = Column(TIMESTAMP, name='created_date', nullable=True)
    default_version = Column(Text, name='default_version', nullable=True)
    description = Column(Text, name='description', nullable=True)
    document_format = Column(Text, name='document_format', nullable=True)
    document_type = Column(Text, name='document_type', nullable=True)
    document_version = Column(Text, name='document_version', nullable=True)
    hash = Column(Text, name='hash', nullable=True)
    hash_type = Column(Text, name='hash_type', nullable=True)
    latest_version = Column(Text, name='latest_version', nullable=True)
    owner = Column(Text, name='owner', nullable=True)
    parameters = Column(JSON, name='parameters', nullable=True)
    pending_review_version = Column(Text, name='pending_review_version', nullable=True)
    platform_types = Column(JSON, name='platform_types', nullable=True)
    requires = Column(JSON, name='requires', nullable=True)
    review_information = Column(JSON, name='review_information', nullable=True)
    review_status = Column(Text, name='review_status', nullable=True)
    schema_version = Column(Text, name='schema_version', nullable=True)
    sha1 = Column(Text, name='sha1', nullable=True)
    status = Column(Text, name='status', nullable=True)
    status_information = Column(Text, name='status_information', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    target_type = Column(Text, name='target_type', nullable=True)
    version_name = Column(Text, name='version_name', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)