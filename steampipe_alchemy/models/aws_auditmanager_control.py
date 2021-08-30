from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAuditmanagerControl(Base, FormatMixins):
    __tablename__ = 'aws_auditmanager_control'
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    last_updated_at = Column('last_updated_at', TIMESTAMP, nullable=True)
    control_mapping_sources = Column('control_mapping_sources', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    action_plan_title = Column('action_plan_title', Text, nullable=True)
    action_plan_instructions = Column('action_plan_instructions', Text, nullable=True)
    control_sources = Column('control_sources', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    last_updated_by = Column('last_updated_by', Text, nullable=True)
    testing_information = Column('testing_information', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    id = Column('id', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)