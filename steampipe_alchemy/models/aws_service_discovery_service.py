from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsServiceDiscoveryService(Base, FormatMixins):
    __tablename__ = 'aws_service_discovery_service'
    _ctx = Column('_ctx', JSON, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    instance_count = Column('instance_count', BigInteger, nullable=True)
    dns_records = Column('dns_records', JSON, nullable=True)
    health_check_config = Column('health_check_config', JSON, nullable=True)
    health_check_custom_config = Column('health_check_custom_config', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    namespace_id = Column('namespace_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    routing_policy = Column('routing_policy', Text, nullable=True)
    name = Column('name', Text, nullable=True)