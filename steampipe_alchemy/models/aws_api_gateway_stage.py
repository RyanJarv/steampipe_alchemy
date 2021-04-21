from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayStage(Base):
    __tablename__ = 'aws_api_gateway_stage'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    rest_api_id = Column(name='rest_api_id', type_=Text, nullable=True)
    deployment_id = Column(name='deployment_id', type_=Text, nullable=True)
    created_date = Column(name='created_date', type_=TIMESTAMP, nullable=True)
    cache_cluster_enabled = Column(name='cache_cluster_enabled', type_=Boolean, nullable=True)
    tracing_enabled = Column(name='tracing_enabled', type_=Boolean, nullable=True)
    access_log_settings = Column(name='access_log_settings', type_=JSON, nullable=True)
    cache_cluster_size = Column(name='cache_cluster_size', type_=Text, nullable=True)
    cache_cluster_status = Column(name='cache_cluster_status', type_=Text, nullable=True)
    client_certificate_id = Column(name='client_certificate_id', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    documentation_version = Column(name='documentation_version', type_=Text, nullable=True)
    last_updated_date = Column(name='last_updated_date', type_=TIMESTAMP, nullable=True)
    canary_settings = Column(name='canary_settings', type_=JSON, nullable=True)
    method_settings = Column(name='method_settings', type_=JSON, nullable=True)
    variables = Column(name='variables', type_=JSON, nullable=True)
    web_acl_arn = Column(name='web_acl_arn', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)