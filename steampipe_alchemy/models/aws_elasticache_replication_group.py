from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsElasticacheReplicationGroup(Base):
    __tablename__ = 'aws_elasticache_replication_group'
    replication_group_id = Column(Text, name='replication_group_id', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    description = Column(Text, name='description', nullable=True)
    at_rest_encryption_enabled = Column(Boolean, name='at_rest_encryption_enabled', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    auth_token_enabled = Column(Boolean, name='auth_token_enabled', nullable=True)
    auth_token_last_modified_date = Column(TIMESTAMP, name='auth_token_last_modified_date', nullable=True)
    automatic_failover = Column(Text, name='automatic_failover', nullable=True)
    cache_node_type = Column(Text, name='cache_node_type', nullable=True)
    cluster_enabled = Column(Boolean, name='cluster_enabled', nullable=True)
    multi_az = Column(Text, name='multi_az', nullable=True)
    snapshot_retention_limit = Column(BigInteger, name='snapshot_retention_limit', nullable=True)
    snapshot_window = Column(Text, name='snapshot_window', nullable=True)
    snapshotting_cluster_id = Column(Text, name='snapshotting_cluster_id', nullable=True)
    status = Column(Text, name='status', nullable=True)
    transit_encryption_enabled = Column(Boolean, name='transit_encryption_enabled', nullable=True)
    configuration_endpoint = Column(JSON, name='configuration_endpoint', nullable=True)
    global_replication_group_info = Column(JSON, name='global_replication_group_info', nullable=True)
    member_clusters = Column(JSON, name='member_clusters', nullable=True)
    member_clusters_outpost_arns = Column(JSON, name='member_clusters_outpost_arns', nullable=True)
    node_groups = Column(JSON, name='node_groups', nullable=True)
    pending_modified_values = Column(JSON, name='pending_modified_values', nullable=True)
    user_group_ids = Column(JSON, name='user_group_ids', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)