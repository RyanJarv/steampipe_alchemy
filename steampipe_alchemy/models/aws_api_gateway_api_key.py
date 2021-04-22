from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayApiKey(Base):
    __tablename__ = 'aws_api_gateway_api_key'
    name = Column('name', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    enabled = Column('enabled', Boolean, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    last_updated_date = Column('last_updated_date', TIMESTAMP, nullable=True)
    customer_id = Column('customer_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    value = Column('value', Text, nullable=True)
    stage_keys = Column('stage_keys', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)