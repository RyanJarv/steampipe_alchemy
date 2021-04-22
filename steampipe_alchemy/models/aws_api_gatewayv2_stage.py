from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayv2Stage(Base):
    __tablename__ = 'aws_api_gatewayv2_stage'
    stage_name = Column('stage_name', Text, nullable=True)
    api_id = Column('api_id', Text, nullable=True)
    api_gateway_managed = Column('api_gateway_managed', Boolean, nullable=True)
    auto_deploy = Column('auto_deploy', Boolean, nullable=True)
    client_certificate_id = Column('client_certificate_id', Text, nullable=True)
    created_date = Column('created_date', Text, nullable=True)
    deployment_id = Column('deployment_id', Text, nullable=True)
    default_route_data_trace_enabled = Column('default_route_data_trace_enabled', Boolean, nullable=True)
    default_route_detailed_metrics_enabled = Column('default_route_detailed_metrics_enabled', Boolean, nullable=True)
    default_route_logging_level = Column('default_route_logging_level', Text, nullable=True)
    default_route_throttling_burst_limit = Column('default_route_throttling_burst_limit', BigInteger, nullable=True)
    default_route_throttling_rate_limit = Column('default_route_throttling_rate_limit', psql.DOUBLE_PRECISION, nullable=True)
    last_deployment_status_message = Column('last_deployment_status_message', Text, nullable=True)
    last_updated_date = Column('last_updated_date', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    stage_variables = Column('stage_variables', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)