from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSsmDocument(Base):
    __tablename__ = 'aws_ssm_document'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    account_ids = Column(name='account_ids', type_=JSON, nullable=True)
    account_sharing_info_list = Column(name='account_sharing_info_list', type_=JSON, nullable=True)
    approved_version = Column(name='approved_version', type_=Text, nullable=True)
    attachments_information = Column(name='attachments_information', type_=JSON, nullable=True)
    author = Column(name='author', type_=Text, nullable=True)
    created_date = Column(name='created_date', type_=TIMESTAMP, nullable=True)
    default_version = Column(name='default_version', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    document_format = Column(name='document_format', type_=Text, nullable=True)
    document_type = Column(name='document_type', type_=Text, nullable=True)
    document_version = Column(name='document_version', type_=Text, nullable=True)
    hash = Column(name='hash', type_=Text, nullable=True)
    hash_type = Column(name='hash_type', type_=Text, nullable=True)
    latest_version = Column(name='latest_version', type_=Text, nullable=True)
    owner = Column(name='owner', type_=Text, nullable=True)
    parameters = Column(name='parameters', type_=JSON, nullable=True)
    pending_review_version = Column(name='pending_review_version', type_=Text, nullable=True)
    platform_types = Column(name='platform_types', type_=JSON, nullable=True)
    requires = Column(name='requires', type_=JSON, nullable=True)
    review_information = Column(name='review_information', type_=JSON, nullable=True)
    review_status = Column(name='review_status', type_=Text, nullable=True)
    schema_version = Column(name='schema_version', type_=Text, nullable=True)
    sha1 = Column(name='sha1', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    status_information = Column(name='status_information', type_=Text, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    target_type = Column(name='target_type', type_=Text, nullable=True)
    version_name = Column(name='version_name', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)