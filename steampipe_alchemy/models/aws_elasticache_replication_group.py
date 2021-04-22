from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticacheReplicationGroup(Base):
    __tablename__ = 'aws_elasticache_replication_group'
    replication_group_id = Column('replication_group_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    at_rest_encryption_enabled = Column('at_rest_encryption_enabled', Boolean, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    auth_token_enabled = Column('auth_token_enabled', Boolean, nullable=True)
    auth_token_last_modified_date = Column('auth_token_last_modified_date', TIMESTAMP, nullable=True)
    automatic_failover = Column('automatic_failover', Text, nullable=True)
    cache_node_type = Column('cache_node_type', Text, nullable=True)
    cluster_enabled = Column('cluster_enabled', Boolean, nullable=True)
    multi_az = Column('multi_az', Text, nullable=True)
    snapshot_retention_limit = Column('snapshot_retention_limit', BigInteger, nullable=True)
    snapshot_window = Column('snapshot_window', Text, nullable=True)
    snapshotting_cluster_id = Column('snapshotting_cluster_id', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    transit_encryption_enabled = Column('transit_encryption_enabled', Boolean, nullable=True)
    configuration_endpoint = Column('configuration_endpoint', JSON, nullable=True)
    global_replication_group_info = Column('global_replication_group_info', JSON, nullable=True)
    member_clusters = Column('member_clusters', JSON, nullable=True)
    member_clusters_outpost_arns = Column('member_clusters_outpost_arns', JSON, nullable=True)
    node_groups = Column('node_groups', JSON, nullable=True)
    pending_modified_values = Column('pending_modified_values', JSON, nullable=True)
    user_group_ids = Column('user_group_ids', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)