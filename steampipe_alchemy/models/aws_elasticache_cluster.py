from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticacheCluster(Base):
    __tablename__ = 'aws_elasticache_cluster'
    cache_cluster_id = Column('cache_cluster_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cache_node_type = Column('cache_node_type', Text, nullable=True)
    cache_cluster_status = Column('cache_cluster_status', Text, nullable=True)
    at_rest_encryption_enabled = Column('at_rest_encryption_enabled', Boolean, nullable=True)
    auth_token_enabled = Column('auth_token_enabled', Boolean, nullable=True)
    auto_minor_version_upgrade = Column('auto_minor_version_upgrade', Boolean, nullable=True)
    cache_cluster_create_time = Column('cache_cluster_create_time', TIMESTAMP, nullable=True)
    cache_subnet_group_name = Column('cache_subnet_group_name', Text, nullable=True)
    client_download_landing_page = Column('client_download_landing_page', Text, nullable=True)
    configuration_endpoint = Column('configuration_endpoint', Text, nullable=True)
    engine = Column('engine', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    num_cache_nodes = Column('num_cache_nodes', BigInteger, nullable=True)
    preferred_availability_zone = Column('preferred_availability_zone', Text, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    transit_encryption_enabled = Column('transit_encryption_enabled', Boolean, nullable=True)
    cache_parameter_group = Column('cache_parameter_group', JSON, nullable=True)
    notification_configuration = Column('notification_configuration', JSON, nullable=True)
    pending_modified_values = Column('pending_modified_values', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)