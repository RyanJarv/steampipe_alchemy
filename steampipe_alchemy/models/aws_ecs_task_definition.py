from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEcsTaskDefinition(Base):
    __tablename__ = 'aws_ecs_task_definition'
    task_definition_arn = Column(name='task_definition_arn', type_=Text, nullable=True)
    cpu = Column(name='cpu', type_=BigInteger, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    execution_role_arn = Column(name='execution_role_arn', type_=Text, nullable=True)
    family = Column(name='family', type_=Text, nullable=True)
    ipc_mode = Column(name='ipc_mode', type_=Text, nullable=True)
    memory = Column(name='memory', type_=BigInteger, nullable=True)
    network_mode = Column(name='network_mode', type_=Text, nullable=True)
    pid_mode = Column(name='pid_mode', type_=Text, nullable=True)
    revision = Column(name='revision', type_=BigInteger, nullable=True)
    task_role_arn = Column(name='task_role_arn', type_=Text, nullable=True)
    registered_at = Column(name='registered_at', type_=Text, nullable=True)
    registered_by = Column(name='registered_by', type_=Text, nullable=True)
    container_definitions = Column(name='container_definitions', type_=JSON, nullable=True)
    compatibilities = Column(name='compatibilities', type_=JSON, nullable=True)
    inference_accelerators = Column(name='inference_accelerators', type_=JSON, nullable=True)
    placement_constraints = Column(name='placement_constraints', type_=JSON, nullable=True)
    proxy_configuration = Column(name='proxy_configuration', type_=JSON, nullable=True)
    requires_attributes = Column(name='requires_attributes', type_=JSON, nullable=True)
    requires_compatibilities = Column(name='requires_compatibilities', type_=JSON, nullable=True)
    volumes = Column(name='volumes', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)