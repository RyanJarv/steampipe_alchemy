from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEcsTaskDefinition(Base):
    __tablename__ = 'aws_ecs_task_definition'
    task_definition_arn = Column(Text, name='task_definition_arn', nullable=True)
    cpu = Column(BigInteger, name='cpu', nullable=True)
    status = Column(Text, name='status', nullable=True)
    execution_role_arn = Column(Text, name='execution_role_arn', nullable=True)
    family = Column(Text, name='family', nullable=True)
    ipc_mode = Column(Text, name='ipc_mode', nullable=True)
    memory = Column(BigInteger, name='memory', nullable=True)
    network_mode = Column(Text, name='network_mode', nullable=True)
    pid_mode = Column(Text, name='pid_mode', nullable=True)
    revision = Column(BigInteger, name='revision', nullable=True)
    task_role_arn = Column(Text, name='task_role_arn', nullable=True)
    registered_at = Column(Text, name='registered_at', nullable=True)
    registered_by = Column(Text, name='registered_by', nullable=True)
    container_definitions = Column(JSON, name='container_definitions', nullable=True)
    compatibilities = Column(JSON, name='compatibilities', nullable=True)
    inference_accelerators = Column(JSON, name='inference_accelerators', nullable=True)
    placement_constraints = Column(JSON, name='placement_constraints', nullable=True)
    proxy_configuration = Column(JSON, name='proxy_configuration', nullable=True)
    requires_attributes = Column(JSON, name='requires_attributes', nullable=True)
    requires_compatibilities = Column(JSON, name='requires_compatibilities', nullable=True)
    volumes = Column(JSON, name='volumes', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)