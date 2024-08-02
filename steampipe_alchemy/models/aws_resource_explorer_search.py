from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsResourceExplorerSearch(Base, FormatMixins):
    __tablename__ = 'aws_resource_explorer_search'
    last_reported_at = Column('last_reported_at', TIMESTAMP, nullable=True)
    properties = Column('properties', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    query = Column('query', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    view_arn = Column('view_arn', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    service = Column('service', Text, nullable=True)
    owning_account_id = Column('owning_account_id', Text, nullable=True)