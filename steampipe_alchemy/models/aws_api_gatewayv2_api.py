from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsApiGatewayv2Api(Base):
    __tablename__ = 'aws_api_gatewayv2_api'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    api_id = Column(Text, name='api_id', nullable=True)
    api_endpoint = Column(Text, name='api_endpoint', nullable=True)
    protocol_type = Column(Text, name='protocol_type', nullable=True)
    api_key_selection_expression = Column(Text, name='api_key_selection_expression', nullable=True)
    route_selection_expression = Column(Text, name='route_selection_expression', nullable=True)
    created_date = Column(TIMESTAMP, name='created_date', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)