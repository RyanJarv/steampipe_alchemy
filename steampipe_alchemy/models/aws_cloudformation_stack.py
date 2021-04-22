from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudformationStack(Base):
    __tablename__ = 'aws_cloudformation_stack'
    id = Column('id', Text, primary_key=True, nullable=True)
    name = Column('name', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    disable_rollback = Column('disable_rollback', Boolean, nullable=True)
    enable_termination_protection = Column('enable_termination_protection', Boolean, nullable=True)
    last_updated_time = Column('last_updated_time', TIMESTAMP, nullable=True)
    parent_id = Column('parent_id', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    root_id = Column('root_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    notification_arns = Column('notification_arns', JSON, nullable=True)
    outputs = Column('outputs', JSON, nullable=True)
    rollback_configuration = Column('rollback_configuration', JSON, nullable=True)
    capabilities = Column('capabilities', JSON, nullable=True)
    stack_drift_status = Column('stack_drift_status', Text, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    template_body = Column('template_body', Text, nullable=True)
    template_body_json = Column('template_body_json', JSON, nullable=True)
    resources = Column('resources', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)