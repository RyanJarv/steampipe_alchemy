from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamAccessAdvisor(Base, FormatMixins):
    __tablename__ = 'aws_iam_access_advisor'
    _ctx = Column('_ctx', JSON, nullable=True)
    last_authenticated = Column('last_authenticated', TIMESTAMP, nullable=True)
    total_authenticated_entities = Column('total_authenticated_entities', BigInteger, nullable=True)
    tracked_actions_last_accessed = Column('tracked_actions_last_accessed', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    last_authenticated_region = Column('last_authenticated_region', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    principal_arn = Column('principal_arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    service_name = Column('service_name', Text, nullable=True)
    service_namespace = Column('service_namespace', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    last_authenticated_entity = Column('last_authenticated_entity', Text, nullable=True)