from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudformationStack(Base):
    __tablename__ = 'aws_cloudformation_stack'
    id = Column(name='id', type_=Text, primary_key=True, nullable=True)
    name = Column(name='name', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    disable_rollback = Column(name='disable_rollback', type_=Boolean, nullable=True)
    enable_termination_protection = Column(name='enable_termination_protection', type_=Boolean, nullable=True)
    last_updated_time = Column(name='last_updated_time', type_=TIMESTAMP, nullable=True)
    parent_id = Column(name='parent_id', type_=Text, nullable=True)
    role_arn = Column(name='role_arn', type_=Text, nullable=True)
    root_id = Column(name='root_id', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    notification_arns = Column(name='notification_arns', type_=JSON, nullable=True)
    outputs = Column(name='outputs', type_=JSON, nullable=True)
    rollback_configuration = Column(name='rollback_configuration', type_=JSON, nullable=True)
    capabilities = Column(name='capabilities', type_=JSON, nullable=True)
    stack_drift_status = Column(name='stack_drift_status', type_=Text, nullable=True)
    parameters = Column(name='parameters', type_=JSON, nullable=True)
    template_body = Column(name='template_body', type_=Text, nullable=True)
    template_body_json = Column(name='template_body_json', type_=JSON, nullable=True)
    resources = Column(name='resources', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)