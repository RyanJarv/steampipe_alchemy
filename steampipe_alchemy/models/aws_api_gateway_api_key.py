from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsApiGatewayApiKey(Base):
    __tablename__ = 'aws_api_gateway_api_key'
    name = Column(Text, name='name', nullable=True)
    id = Column(Text, name='id', primary_key=True, nullable=True)
    enabled = Column(Boolean, name='enabled', nullable=True)
    created_date = Column(TIMESTAMP, name='created_date', nullable=True)
    last_updated_date = Column(TIMESTAMP, name='last_updated_date', nullable=True)
    customer_id = Column(Text, name='customer_id', nullable=True)
    description = Column(Text, name='description', nullable=True)
    value = Column(Text, name='value', nullable=True)
    stage_keys = Column(JSON, name='stage_keys', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)