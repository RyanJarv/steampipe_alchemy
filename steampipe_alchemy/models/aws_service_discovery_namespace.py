from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsServiceDiscoveryNamespace(Base, FormatMixins):
    __tablename__ = 'aws_service_discovery_namespace'
    _ctx = Column('_ctx', JSON, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    service_count = Column('service_count', BigInteger, nullable=True)
    dns_properties = Column('dns_properties', JSON, nullable=True)
    http_properties = Column('http_properties', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)