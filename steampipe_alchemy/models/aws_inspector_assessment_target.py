from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsInspectorAssessmentTarget(Base):
    __tablename__ = 'aws_inspector_assessment_target'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    resource_group_arn = Column(name='resource_group_arn', type_=Text, nullable=True)
    created_at = Column(name='created_at', type_=TIMESTAMP, nullable=True)
    updated_at = Column(name='updated_at', type_=TIMESTAMP, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)