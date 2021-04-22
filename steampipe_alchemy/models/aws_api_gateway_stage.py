from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayStage(Base):
    __tablename__ = 'aws_api_gateway_stage'
    name = Column('name', Text, primary_key=True, nullable=True)
    rest_api_id = Column('rest_api_id', Text, nullable=True)
    deployment_id = Column('deployment_id', Text, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    cache_cluster_enabled = Column('cache_cluster_enabled', Boolean, nullable=True)
    tracing_enabled = Column('tracing_enabled', Boolean, nullable=True)
    access_log_settings = Column('access_log_settings', JSON, nullable=True)
    cache_cluster_size = Column('cache_cluster_size', Text, nullable=True)
    cache_cluster_status = Column('cache_cluster_status', Text, nullable=True)
    client_certificate_id = Column('client_certificate_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    documentation_version = Column('documentation_version', Text, nullable=True)
    last_updated_date = Column('last_updated_date', TIMESTAMP, nullable=True)
    canary_settings = Column('canary_settings', JSON, nullable=True)
    method_settings = Column('method_settings', JSON, nullable=True)
    variables = Column('variables', JSON, nullable=True)
    web_acl_arn = Column('web_acl_arn', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)