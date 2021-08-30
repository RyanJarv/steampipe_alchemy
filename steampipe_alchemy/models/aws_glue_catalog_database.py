from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlueCatalogDatabase(Base, FormatMixins):
    __tablename__ = 'aws_glue_catalog_database'
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    create_table_default_permissions = Column('create_table_default_permissions', JSON, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    target_database = Column('target_database', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    catalog_id = Column('catalog_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    location_uri = Column('location_uri', Text, nullable=True)
    title = Column('title', Text, nullable=True)