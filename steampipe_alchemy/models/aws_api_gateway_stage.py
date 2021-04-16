from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsApiGatewayStage(Base):
    __tablename__ = 'aws_api_gateway_stage'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    rest_api_id = Column(Text, name='rest_api_id', nullable=True)
    deployment_id = Column(Text, name='deployment_id', nullable=True)
    created_date = Column(TIMESTAMP, name='created_date', nullable=True)
    cache_cluster_enabled = Column(Boolean, name='cache_cluster_enabled', nullable=True)
    tracing_enabled = Column(Boolean, name='tracing_enabled', nullable=True)
    access_log_settings = Column(JSON, name='access_log_settings', nullable=True)
    cache_cluster_size = Column(Text, name='cache_cluster_size', nullable=True)
    cache_cluster_status = Column(Text, name='cache_cluster_status', nullable=True)
    client_certificate_id = Column(Text, name='client_certificate_id', nullable=True)
    description = Column(Text, name='description', nullable=True)
    documentation_version = Column(Text, name='documentation_version', nullable=True)
    last_updated_date = Column(TIMESTAMP, name='last_updated_date', nullable=True)
    canary_settings = Column(JSON, name='canary_settings', nullable=True)
    method_settings = Column(JSON, name='method_settings', nullable=True)
    variables = Column(JSON, name='variables', nullable=True)
    web_acl_arn = Column(Text, name='web_acl_arn', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)