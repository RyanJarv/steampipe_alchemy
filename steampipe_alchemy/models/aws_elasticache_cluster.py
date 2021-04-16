from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsElasticacheCluster(Base):
    __tablename__ = 'aws_elasticache_cluster'
    cache_cluster_id = Column(Text, name='cache_cluster_id', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    cache_node_type = Column(Text, name='cache_node_type', nullable=True)
    cache_cluster_status = Column(Text, name='cache_cluster_status', nullable=True)
    at_rest_encryption_enabled = Column(Boolean, name='at_rest_encryption_enabled', nullable=True)
    auth_token_enabled = Column(Boolean, name='auth_token_enabled', nullable=True)
    auto_minor_version_upgrade = Column(Boolean, name='auto_minor_version_upgrade', nullable=True)
    cache_cluster_create_time = Column(TIMESTAMP, name='cache_cluster_create_time', nullable=True)
    cache_subnet_group_name = Column(Text, name='cache_subnet_group_name', nullable=True)
    client_download_landing_page = Column(Text, name='client_download_landing_page', nullable=True)
    configuration_endpoint = Column(Text, name='configuration_endpoint', nullable=True)
    engine = Column(Text, name='engine', nullable=True)
    engine_version = Column(Text, name='engine_version', nullable=True)
    num_cache_nodes = Column(BigInteger, name='num_cache_nodes', nullable=True)
    preferred_availability_zone = Column(Text, name='preferred_availability_zone', nullable=True)
    preferred_maintenance_window = Column(Text, name='preferred_maintenance_window', nullable=True)
    transit_encryption_enabled = Column(Boolean, name='transit_encryption_enabled', nullable=True)
    cache_parameter_group = Column(JSON, name='cache_parameter_group', nullable=True)
    notification_configuration = Column(JSON, name='notification_configuration', nullable=True)
    pending_modified_values = Column(JSON, name='pending_modified_values', nullable=True)
    security_groups = Column(JSON, name='security_groups', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)