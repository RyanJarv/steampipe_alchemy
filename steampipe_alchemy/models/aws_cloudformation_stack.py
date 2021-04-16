from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsCloudformationStack(Base):
    __tablename__ = 'aws_cloudformation_stack'
    id = Column(Text, name='id', primary_key=True, nullable=True)
    name = Column(Text, name='name', nullable=True)
    status = Column(Text, name='status', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    disable_rollback = Column(Boolean, name='disable_rollback', nullable=True)
    enable_termination_protection = Column(Boolean, name='enable_termination_protection', nullable=True)
    last_updated_time = Column(TIMESTAMP, name='last_updated_time', nullable=True)
    parent_id = Column(Text, name='parent_id', nullable=True)
    role_arn = Column(Text, name='role_arn', nullable=True)
    root_id = Column(Text, name='root_id', nullable=True)
    description = Column(Text, name='description', nullable=True)
    notification_arns = Column(JSON, name='notification_arns', nullable=True)
    outputs = Column(JSON, name='outputs', nullable=True)
    rollback_configuration = Column(JSON, name='rollback_configuration', nullable=True)
    capabilities = Column(JSON, name='capabilities', nullable=True)
    stack_drift_status = Column(Text, name='stack_drift_status', nullable=True)
    parameters = Column(JSON, name='parameters', nullable=True)
    template_body = Column(Text, name='template_body', nullable=True)
    template_body_json = Column(JSON, name='template_body_json', nullable=True)
    resources = Column(JSON, name='resources', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)