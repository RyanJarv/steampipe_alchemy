from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayv2Stage(Base):
    __tablename__ = 'aws_api_gatewayv2_stage'
    stage_name = Column(name='stage_name', type_=Text, nullable=True)
    api_id = Column(name='api_id', type_=Text, nullable=True)
    api_gateway_managed = Column(name='api_gateway_managed', type_=Boolean, nullable=True)
    auto_deploy = Column(name='auto_deploy', type_=Boolean, nullable=True)
    client_certificate_id = Column(name='client_certificate_id', type_=Text, nullable=True)
    created_date = Column(name='created_date', type_=Text, nullable=True)
    deployment_id = Column(name='deployment_id', type_=Text, nullable=True)
    default_route_data_trace_enabled = Column(name='default_route_data_trace_enabled', type_=Boolean, nullable=True)
    default_route_detailed_metrics_enabled = Column(name='default_route_detailed_metrics_enabled', type_=Boolean, nullable=True)
    default_route_logging_level = Column(name='default_route_logging_level', type_=Text, nullable=True)
    default_route_throttling_burst_limit = Column(name='default_route_throttling_burst_limit', type_=BigInteger, nullable=True)
    default_route_throttling_rate_limit = Column(name='default_route_throttling_rate_limit', type_=psql.DOUBLE_PRECISION, nullable=True)
    last_deployment_status_message = Column(name='last_deployment_status_message', type_=Text, nullable=True)
    last_updated_date = Column(name='last_updated_date', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    stage_variables = Column(name='stage_variables', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)