from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayv2Api(Base):
    __tablename__ = 'aws_api_gatewayv2_api'
    name = Column('name', Text, primary_key=True, nullable=True)
    api_id = Column('api_id', Text, nullable=True)
    api_endpoint = Column('api_endpoint', Text, nullable=True)
    protocol_type = Column('protocol_type', Text, nullable=True)
    api_key_selection_expression = Column('api_key_selection_expression', Text, nullable=True)
    route_selection_expression = Column('route_selection_expression', Text, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)