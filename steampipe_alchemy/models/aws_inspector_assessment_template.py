from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsInspectorAssessmentTemplate(Base, FormatMixins):
    __tablename__ = 'aws_inspector_assessment_template'
    tags_src = Column('tags_src', JSON, nullable=True)
    event_subscriptions = Column('event_subscriptions', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    duration_in_seconds = Column('duration_in_seconds', BigInteger, nullable=True)
    assessment_run_count = Column('assessment_run_count', BigInteger, nullable=True)
    rules_package_arns = Column('rules_package_arns', JSON, nullable=True)
    user_attributes_for_findings = Column('user_attributes_for_findings', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    assessment_target_arn = Column('assessment_target_arn', Text, nullable=True)
    last_assessment_run_arn = Column('last_assessment_run_arn', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)