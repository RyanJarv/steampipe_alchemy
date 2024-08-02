from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEksNodeGroup(Base, FormatMixins):
    __tablename__ = 'aws_eks_node_group'
    _ctx = Column('_ctx', JSON, nullable=True)
    modified_at = Column('modified_at', TIMESTAMP, nullable=True)
    health = Column('health', JSON, nullable=True)
    instance_types = Column('instance_types', JSON, nullable=True)
    labels = Column('labels', JSON, nullable=True)
    launch_template = Column('launch_template', JSON, nullable=True)
    remote_access = Column('remote_access', JSON, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    scaling_config = Column('scaling_config', JSON, nullable=True)
    subnets = Column('subnets', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    taints = Column('taints', JSON, nullable=True)
    update_config = Column('update_config', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    disk_size = Column('disk_size', BigInteger, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cluster_name = Column('cluster_name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    ami_type = Column('ami_type', Text, nullable=True)
    capacity_type = Column('capacity_type', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    node_role = Column('node_role', Text, nullable=True)
    release_version = Column('release_version', Text, nullable=True)
    version = Column('version', Text, nullable=True)
    nodegroup_name = Column('nodegroup_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)