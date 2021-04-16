from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsApiGatewayv2Stage(Base):
    __tablename__ = 'aws_api_gatewayv2_stage'
    stage_name = Column(Text, name='stage_name', nullable=True)
    api_id = Column(Text, name='api_id', nullable=True)
    api_gateway_managed = Column(Boolean, name='api_gateway_managed', nullable=True)
    auto_deploy = Column(Boolean, name='auto_deploy', nullable=True)
    client_certificate_id = Column(Text, name='client_certificate_id', nullable=True)
    created_date = Column(Text, name='created_date', nullable=True)
    deployment_id = Column(Text, name='deployment_id', nullable=True)
    default_route_data_trace_enabled = Column(Boolean, name='default_route_data_trace_enabled', nullable=True)
    default_route_detailed_metrics_enabled = Column(Boolean, name='default_route_detailed_metrics_enabled', nullable=True)
    default_route_logging_level = Column(Text, name='default_route_logging_level', nullable=True)
    default_route_throttling_burst_limit = Column(BigInteger, name='default_route_throttling_burst_limit', nullable=True)
    default_route_throttling_rate_limit = Column(psql.DOUBLE_PRECISION, name='default_route_throttling_rate_limit', nullable=True)
    last_deployment_status_message = Column(Text, name='last_deployment_status_message', nullable=True)
    last_updated_date = Column(Text, name='last_updated_date', nullable=True)
    description = Column(Text, name='description', nullable=True)
    stage_variables = Column(JSON, name='stage_variables', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)