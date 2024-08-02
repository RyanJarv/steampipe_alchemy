from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodedeployDeploymentConfig(Base, FormatMixins):
    __tablename__ = 'aws_codedeploy_deployment_config'
    akas = Column('akas', JSON, nullable=True)
    compute_platform = Column('compute_platform', JSON, nullable=True)
    minimum_healthy_hosts = Column('minimum_healthy_hosts', JSON, nullable=True)
    traffic_routing_config = Column('traffic_routing_config', JSON, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    deployment_config_id = Column('deployment_config_id', Text, nullable=True)
    deployment_config_name = Column('deployment_config_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)