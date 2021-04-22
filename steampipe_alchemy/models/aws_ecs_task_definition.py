from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEcsTaskDefinition(Base):
    __tablename__ = 'aws_ecs_task_definition'
    task_definition_arn = Column('task_definition_arn', Text, nullable=True)
    cpu = Column('cpu', BigInteger, nullable=True)
    status = Column('status', Text, nullable=True)
    execution_role_arn = Column('execution_role_arn', Text, nullable=True)
    family = Column('family', Text, nullable=True)
    ipc_mode = Column('ipc_mode', Text, nullable=True)
    memory = Column('memory', BigInteger, nullable=True)
    network_mode = Column('network_mode', Text, nullable=True)
    pid_mode = Column('pid_mode', Text, nullable=True)
    revision = Column('revision', BigInteger, nullable=True)
    task_role_arn = Column('task_role_arn', Text, nullable=True)
    registered_at = Column('registered_at', Text, nullable=True)
    registered_by = Column('registered_by', Text, nullable=True)
    container_definitions = Column('container_definitions', JSON, nullable=True)
    compatibilities = Column('compatibilities', JSON, nullable=True)
    inference_accelerators = Column('inference_accelerators', JSON, nullable=True)
    placement_constraints = Column('placement_constraints', JSON, nullable=True)
    proxy_configuration = Column('proxy_configuration', JSON, nullable=True)
    requires_attributes = Column('requires_attributes', JSON, nullable=True)
    requires_compatibilities = Column('requires_compatibilities', JSON, nullable=True)
    volumes = Column('volumes', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)