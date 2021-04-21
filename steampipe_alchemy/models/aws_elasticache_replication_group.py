from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsElasticacheReplicationGroup(Base):
    __tablename__ = 'aws_elasticache_replication_group'
    replication_group_id = Column(name='replication_group_id', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    at_rest_encryption_enabled = Column(name='at_rest_encryption_enabled', type_=Boolean, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    auth_token_enabled = Column(name='auth_token_enabled', type_=Boolean, nullable=True)
    auth_token_last_modified_date = Column(name='auth_token_last_modified_date', type_=TIMESTAMP, nullable=True)
    automatic_failover = Column(name='automatic_failover', type_=Text, nullable=True)
    cache_node_type = Column(name='cache_node_type', type_=Text, nullable=True)
    cluster_enabled = Column(name='cluster_enabled', type_=Boolean, nullable=True)
    multi_az = Column(name='multi_az', type_=Text, nullable=True)
    snapshot_retention_limit = Column(name='snapshot_retention_limit', type_=BigInteger, nullable=True)
    snapshot_window = Column(name='snapshot_window', type_=Text, nullable=True)
    snapshotting_cluster_id = Column(name='snapshotting_cluster_id', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    transit_encryption_enabled = Column(name='transit_encryption_enabled', type_=Boolean, nullable=True)
    configuration_endpoint = Column(name='configuration_endpoint', type_=JSON, nullable=True)
    global_replication_group_info = Column(name='global_replication_group_info', type_=JSON, nullable=True)
    member_clusters = Column(name='member_clusters', type_=JSON, nullable=True)
    member_clusters_outpost_arns = Column(name='member_clusters_outpost_arns', type_=JSON, nullable=True)
    node_groups = Column(name='node_groups', type_=JSON, nullable=True)
    pending_modified_values = Column(name='pending_modified_values', type_=JSON, nullable=True)
    user_group_ids = Column(name='user_group_ids', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)