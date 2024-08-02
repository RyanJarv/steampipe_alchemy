from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsApiGatewayMethod(Base, FormatMixins):
    __tablename__ = 'aws_api_gateway_method'
    _ctx = Column('_ctx', JSON, nullable=True)
    api_key_required = Column('api_key_required', Boolean, nullable=True)
    authorization_scopes = Column('authorization_scopes', JSON, nullable=True)
    method_integration = Column('method_integration', JSON, nullable=True)
    method_responses = Column('method_responses', JSON, nullable=True)
    request_models = Column('request_models', JSON, nullable=True)
    request_parameters = Column('request_parameters', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    operation_name = Column('operation_name', Text, nullable=True)
    request_validator_id = Column('request_validator_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    rest_api_id = Column('rest_api_id', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)
    http_method = Column('http_method', Text, nullable=True)
    path = Column('path', Text, nullable=True)
    path_part = Column('path_part', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    authorization_type = Column('authorization_type', Text, nullable=True)
    authorizer_id = Column('authorizer_id', Text, nullable=True)