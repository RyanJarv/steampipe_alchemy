from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsInspectorAssessmentTarget(Base):
    __tablename__ = 'aws_inspector_assessment_target'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    resource_group_arn = Column(Text, name='resource_group_arn', nullable=True)
    created_at = Column(TIMESTAMP, name='created_at', nullable=True)
    updated_at = Column(TIMESTAMP, name='updated_at', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)