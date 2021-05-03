from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsInspectorAssessmentTarget(Base, FormatMixins):
    __tablename__ = 'aws_inspector_assessment_target'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    resource_group_arn = Column('resource_group_arn', Text, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)