from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsApiGatewayv2Integration(Base, FormatMixins):
    __tablename__ = 'aws_api_gatewayv2_integration'
    response_parameters = Column('response_parameters', JSON, nullable=True)
    tls_config = Column('tls_config', JSON, nullable=True)
    api_gateway_managed = Column('api_gateway_managed', Boolean, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    timeout_in_millis = Column('timeout_in_millis', BigInteger, nullable=True)
    request_parameters = Column('request_parameters', JSON, nullable=True)
    request_templates = Column('request_templates', JSON, nullable=True)
    connection_id = Column('connection_id', Text, nullable=True)
    connection_type = Column('connection_type', Text, nullable=True)
    content_handling_strategy = Column('content_handling_strategy', Text, nullable=True)
    credentials_arn = Column('credentials_arn', Text, nullable=True)
    integration_response_selection_expression = Column('integration_response_selection_expression', Text, nullable=True)
    integration_subtype = Column('integration_subtype', Text, nullable=True)
    passthrough_behavior = Column('passthrough_behavior', Text, nullable=True)
    payload_format_version = Column('payload_format_version', Text, nullable=True)
    template_selection_expression = Column('template_selection_expression', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    integration_id = Column('integration_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    api_id = Column('api_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    integration_method = Column('integration_method', Text, nullable=True)
    integration_type = Column('integration_type', Text, nullable=True)
    integration_uri = Column('integration_uri', Text, nullable=True)