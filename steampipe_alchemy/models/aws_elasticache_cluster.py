from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticacheCluster(Base):
    __tablename__ = 'aws_elasticache_cluster'
    cache_cluster_id = Column(name='cache_cluster_id', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    cache_node_type = Column(name='cache_node_type', type_=Text, nullable=True)
    cache_cluster_status = Column(name='cache_cluster_status', type_=Text, nullable=True)
    at_rest_encryption_enabled = Column(name='at_rest_encryption_enabled', type_=Boolean, nullable=True)
    auth_token_enabled = Column(name='auth_token_enabled', type_=Boolean, nullable=True)
    auto_minor_version_upgrade = Column(name='auto_minor_version_upgrade', type_=Boolean, nullable=True)
    cache_cluster_create_time = Column(name='cache_cluster_create_time', type_=TIMESTAMP, nullable=True)
    cache_subnet_group_name = Column(name='cache_subnet_group_name', type_=Text, nullable=True)
    client_download_landing_page = Column(name='client_download_landing_page', type_=Text, nullable=True)
    configuration_endpoint = Column(name='configuration_endpoint', type_=Text, nullable=True)
    engine = Column(name='engine', type_=Text, nullable=True)
    engine_version = Column(name='engine_version', type_=Text, nullable=True)
    num_cache_nodes = Column(name='num_cache_nodes', type_=BigInteger, nullable=True)
    preferred_availability_zone = Column(name='preferred_availability_zone', type_=Text, nullable=True)
    preferred_maintenance_window = Column(name='preferred_maintenance_window', type_=Text, nullable=True)
    transit_encryption_enabled = Column(name='transit_encryption_enabled', type_=Boolean, nullable=True)
    cache_parameter_group = Column(name='cache_parameter_group', type_=JSON, nullable=True)
    notification_configuration = Column(name='notification_configuration', type_=JSON, nullable=True)
    pending_modified_values = Column(name='pending_modified_values', type_=JSON, nullable=True)
    security_groups = Column(name='security_groups', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)