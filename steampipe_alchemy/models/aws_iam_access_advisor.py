from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamAccessAdvisor(Base):
    __tablename__ = 'aws_iam_access_advisor'
    principal_arn = Column(name='principal_arn', type_=Text, primary_key=True, nullable=True)
    service_name = Column(name='service_name', type_=Text, nullable=True)
    service_namespace = Column(name='service_namespace', type_=Text, nullable=True)
    last_authenticated = Column(name='last_authenticated', type_=TIMESTAMP, nullable=True)
    last_authenticated_entity = Column(name='last_authenticated_entity', type_=Text, nullable=True)
    last_authenticated_region = Column(name='last_authenticated_region', type_=Text, nullable=True)
    total_authenticated_entities = Column(name='total_authenticated_entities', type_=BigInteger, nullable=True)
    tracked_actions_last_accessed = Column(name='tracked_actions_last_accessed', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)