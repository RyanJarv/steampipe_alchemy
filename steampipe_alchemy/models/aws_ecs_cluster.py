from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEcsCluster(Base):
    __tablename__ = 'aws_ecs_cluster'
    cluster_arn = Column(name='cluster_arn', type_=Text, nullable=True)
    cluster_name = Column(name='cluster_name', type_=Text, nullable=True)
    active_services_count = Column(name='active_services_count', type_=BigInteger, nullable=True)
    pending_tasks_count = Column(name='pending_tasks_count', type_=BigInteger, nullable=True)
    registered_container_instances_count = Column(name='registered_container_instances_count', type_=BigInteger, nullable=True)
    running_tasks_count = Column(name='running_tasks_count', type_=BigInteger, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    attachments_status = Column(name='attachments_status', type_=Text, nullable=True)
    attachments = Column(name='attachments', type_=JSON, nullable=True)
    capacity_providers = Column(name='capacity_providers', type_=JSON, nullable=True)
    default_capacity_provider_strategy = Column(name='default_capacity_provider_strategy', type_=JSON, nullable=True)
    settings = Column(name='settings', type_=JSON, nullable=True)
    statistics = Column(name='statistics', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)