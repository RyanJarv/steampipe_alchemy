from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsInspectorExclusion(Base, FormatMixins):
    __tablename__ = 'aws_inspector_exclusion'
    _ctx = Column('_ctx', JSON, nullable=True)
    attributes = Column('attributes', JSON, nullable=True)
    scopes = Column('scopes', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    assessment_run_arn = Column('assessment_run_arn', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    recommendation = Column('recommendation', Text, nullable=True)