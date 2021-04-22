from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEcsCluster(Base):
    __tablename__ = 'aws_ecs_cluster'
    cluster_arn = Column('cluster_arn', Text, nullable=True)
    cluster_name = Column('cluster_name', Text, nullable=True)
    active_services_count = Column('active_services_count', BigInteger, nullable=True)
    pending_tasks_count = Column('pending_tasks_count', BigInteger, nullable=True)
    registered_container_instances_count = Column('registered_container_instances_count', BigInteger, nullable=True)
    running_tasks_count = Column('running_tasks_count', BigInteger, nullable=True)
    status = Column('status', Text, nullable=True)
    attachments_status = Column('attachments_status', Text, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    capacity_providers = Column('capacity_providers', JSON, nullable=True)
    default_capacity_provider_strategy = Column('default_capacity_provider_strategy', JSON, nullable=True)
    settings = Column('settings', JSON, nullable=True)
    statistics = Column('statistics', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)