from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsApiGatewayv2Route(Base, FormatMixins):
    __tablename__ = 'aws_api_gatewayv2_route'
    _ctx = Column('_ctx', JSON, nullable=True)
    api_gateway_managed = Column('api_gateway_managed', Boolean, nullable=True)
    api_key_required = Column('api_key_required', Boolean, nullable=True)
    authorization_scopes = Column('authorization_scopes', JSON, nullable=True)
    request_models = Column('request_models', JSON, nullable=True)
    request_parameters = Column('request_parameters', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    operation_name = Column('operation_name', Text, nullable=True)
    route_response_selection_expression = Column('route_response_selection_expression', Text, nullable=True)
    target = Column('target', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    api_id = Column('api_id', Text, nullable=True)
    route_id = Column('route_id', Text, nullable=True)
    route_key = Column('route_key', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    authorization_type = Column('authorization_type', Text, nullable=True)
    authorizer_id = Column('authorizer_id', Text, nullable=True)
    model_selection_expression = Column('model_selection_expression', Text, nullable=True)