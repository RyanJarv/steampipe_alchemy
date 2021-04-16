from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEcsCluster(Base):
    __tablename__ = 'aws_ecs_cluster'
    cluster_arn = Column(Text, name='cluster_arn', nullable=True)
    cluster_name = Column(Text, name='cluster_name', nullable=True)
    active_services_count = Column(BigInteger, name='active_services_count', nullable=True)
    pending_tasks_count = Column(BigInteger, name='pending_tasks_count', nullable=True)
    registered_container_instances_count = Column(BigInteger, name='registered_container_instances_count', nullable=True)
    running_tasks_count = Column(BigInteger, name='running_tasks_count', nullable=True)
    status = Column(Text, name='status', nullable=True)
    attachments_status = Column(Text, name='attachments_status', nullable=True)
    attachments = Column(JSON, name='attachments', nullable=True)
    capacity_providers = Column(JSON, name='capacity_providers', nullable=True)
    default_capacity_provider_strategy = Column(JSON, name='default_capacity_provider_strategy', nullable=True)
    settings = Column(JSON, name='settings', nullable=True)
    statistics = Column(JSON, name='statistics', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)