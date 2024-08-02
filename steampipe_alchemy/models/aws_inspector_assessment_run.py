from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsInspectorAssessmentRun(Base, FormatMixins):
    __tablename__ = 'aws_inspector_assessment_run'
    _ctx = Column('_ctx', JSON, nullable=True)
    started_at = Column('started_at', TIMESTAMP, nullable=True)
    state_changed_at = Column('state_changed_at', TIMESTAMP, nullable=True)
    finding_counts = Column('finding_counts', JSON, nullable=True)
    notifications = Column('notifications', JSON, nullable=True)
    rules_package_arns = Column('rules_package_arns', JSON, nullable=True)
    state_changes = Column('state_changes', JSON, nullable=True)
    user_attributes_for_findings = Column('user_attributes_for_findings', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    completed_at = Column('completed_at', TIMESTAMP, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    data_collected = Column('data_collected', Boolean, nullable=True)
    duration_in_seconds = Column('duration_in_seconds', BigInteger, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    assessment_template_arn = Column('assessment_template_arn', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)