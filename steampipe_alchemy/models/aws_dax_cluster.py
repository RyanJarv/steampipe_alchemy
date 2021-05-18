from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsDaxCluster(Base, FormatMixins):
    __tablename__ = 'aws_dax_cluster'
    cluster_name = Column('cluster_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    active_nodes = Column('active_nodes', BigInteger, nullable=True)
    iam_role_arn = Column('iam_role_arn', Text, nullable=True)
    node_type = Column('node_type', Text, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    subnet_group = Column('subnet_group', Text, nullable=True)
    total_nodes = Column('total_nodes', Text, nullable=True)
    cluster_discovery_endpoint = Column('cluster_discovery_endpoint', JSON, nullable=True)
    node_ids_to_remove = Column('node_ids_to_remove', JSON, nullable=True)
    nodes = Column('nodes', JSON, nullable=True)
    notification_configuration = Column('notification_configuration', JSON, nullable=True)
    parameter_group = Column('parameter_group', JSON, nullable=True)
    sse_description = Column('sse_description', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsDaxClusterLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_dax_cluster_local'
    cluster_name = Column('cluster_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    active_nodes = Column('active_nodes', BigInteger, nullable=True)
    iam_role_arn = Column('iam_role_arn', Text, nullable=True)
    node_type = Column('node_type', Text, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    subnet_group = Column('subnet_group', Text, nullable=True)
    total_nodes = Column('total_nodes', Text, nullable=True)
    cluster_discovery_endpoint = Column('cluster_discovery_endpoint', JSON, nullable=True)
    node_ids_to_remove = Column('node_ids_to_remove', JSON, nullable=True)
    nodes = Column('nodes', JSON, nullable=True)
    notification_configuration = Column('notification_configuration', JSON, nullable=True)
    parameter_group = Column('parameter_group', JSON, nullable=True)
    sse_description = Column('sse_description', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsDaxCluster).select_from(AwsDaxCluster)
create_materialized_view('aws_dax_cluster_local', cache, db.metadata_materialized)
