from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamAccessAdvisor(Base):
    __tablename__ = 'aws_iam_access_advisor'
    principal_arn = Column(Text, name='principal_arn', primary_key=True, nullable=True)
    service_name = Column(Text, name='service_name', nullable=True)
    service_namespace = Column(Text, name='service_namespace', nullable=True)
    last_authenticated = Column(TIMESTAMP, name='last_authenticated', nullable=True)
    last_authenticated_entity = Column(Text, name='last_authenticated_entity', nullable=True)
    last_authenticated_region = Column(Text, name='last_authenticated_region', nullable=True)
    total_authenticated_entities = Column(BigInteger, name='total_authenticated_entities', nullable=True)
    tracked_actions_last_accessed = Column(JSON, name='tracked_actions_last_accessed', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)