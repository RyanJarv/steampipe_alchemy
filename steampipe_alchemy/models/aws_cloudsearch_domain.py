from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudsearchDomain(Base, FormatMixins):
    __tablename__ = 'aws_cloudsearch_domain'
    _ctx = Column('_ctx', JSON, nullable=True)
    processing = Column('processing', Boolean, nullable=True)
    requires_index_documents = Column('requires_index_documents', Boolean, nullable=True)
    search_instance_count = Column('search_instance_count', BigInteger, nullable=True)
    search_partition_count = Column('search_partition_count', BigInteger, nullable=True)
    doc_service = Column('doc_service', JSON, nullable=True)
    limits = Column('limits', JSON, nullable=True)
    search_service = Column('search_service', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    created = Column('created', Boolean, nullable=True)
    deleted = Column('deleted', Boolean, nullable=True)
    domain_id = Column('domain_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    search_instance_type = Column('search_instance_type', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)