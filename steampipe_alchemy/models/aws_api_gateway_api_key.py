from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayApiKey(Base):
    __tablename__ = 'aws_api_gateway_api_key'
    name = Column(name='name', type_=Text, nullable=True)
    id = Column(name='id', type_=Text, primary_key=True, nullable=True)
    enabled = Column(name='enabled', type_=Boolean, nullable=True)
    created_date = Column(name='created_date', type_=TIMESTAMP, nullable=True)
    last_updated_date = Column(name='last_updated_date', type_=TIMESTAMP, nullable=True)
    customer_id = Column(name='customer_id', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    value = Column(name='value', type_=Text, nullable=True)
    stage_keys = Column(name='stage_keys', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)