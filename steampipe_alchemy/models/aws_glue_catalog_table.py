from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlueCatalogTable(Base, FormatMixins):
    __tablename__ = 'aws_glue_catalog_table'
    last_analyzed_time = Column('last_analyzed_time', TIMESTAMP, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    partition_keys = Column('partition_keys', JSON, nullable=True)
    storage_descriptor = Column('storage_descriptor', JSON, nullable=True)
    target_table = Column('target_table', JSON, nullable=True)
    lf_tags = Column('lf_tags', JSON, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    retention = Column('retention', BigInteger, nullable=True)
    is_registered_with_lake_formation = Column('is_registered_with_lake_formation', Boolean, nullable=True)
    update_time = Column('update_time', TIMESTAMP, nullable=True)
    last_access_time = Column('last_access_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    view_original_text = Column('view_original_text', Text, nullable=True)
    catalog_id = Column('catalog_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    database_name = Column('database_name', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    table_type = Column('table_type', Text, nullable=True)
    view_expanded_text = Column('view_expanded_text', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)