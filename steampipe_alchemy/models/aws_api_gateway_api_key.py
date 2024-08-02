from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsApiGatewayApiKey(Base, FormatMixins):
    __tablename__ = 'aws_api_gateway_api_key'
    _ctx = Column('_ctx', JSON, nullable=True)
    enabled = Column('enabled', Boolean, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    last_updated_date = Column('last_updated_date', TIMESTAMP, nullable=True)
    stage_keys = Column('stage_keys', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    customer_id = Column('customer_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    value = Column('value', Text, nullable=True)
    region = Column('region', Text, nullable=True)