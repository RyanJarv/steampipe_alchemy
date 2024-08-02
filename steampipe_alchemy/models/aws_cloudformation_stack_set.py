from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudformationStackSet(Base, FormatMixins):
    __tablename__ = 'aws_cloudformation_stack_set'
    _ctx = Column('_ctx', JSON, nullable=True)
    last_drift_check_timestamp = Column('last_drift_check_timestamp', TIMESTAMP, nullable=True)
    auto_deployment = Column('auto_deployment', JSON, nullable=True)
    capabilities = Column('capabilities', JSON, nullable=True)
    organizational_unit_ids = Column('organizational_unit_ids', JSON, nullable=True)
    parameters = Column('parameters', JSON, nullable=True)
    stack_set_drift_detection_details = Column('stack_set_drift_detection_details', JSON, nullable=True)
    managed_execution = Column('managed_execution', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    stack_set_id = Column('stack_set_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    stack_set_name = Column('stack_set_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    drift_status = Column('drift_status', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    permission_model = Column('permission_model', Text, nullable=True)
    administration_role_arn = Column('administration_role_arn', Text, nullable=True)
    execution_role_name = Column('execution_role_name', Text, nullable=True)
    template_body = Column('template_body', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)