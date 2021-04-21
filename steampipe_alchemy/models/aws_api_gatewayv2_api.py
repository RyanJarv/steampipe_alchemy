from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayv2Api(Base):
    __tablename__ = 'aws_api_gatewayv2_api'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    api_id = Column(name='api_id', type_=Text, nullable=True)
    api_endpoint = Column(name='api_endpoint', type_=Text, nullable=True)
    protocol_type = Column(name='protocol_type', type_=Text, nullable=True)
    api_key_selection_expression = Column(name='api_key_selection_expression', type_=Text, nullable=True)
    route_selection_expression = Column(name='route_selection_expression', type_=Text, nullable=True)
    created_date = Column(name='created_date', type_=TIMESTAMP, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)