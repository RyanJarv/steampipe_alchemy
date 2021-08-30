from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAccessanalyzerAnalyzer(Base, FormatMixins):
    __tablename__ = 'aws_accessanalyzer_analyzer'
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    findings = Column('findings', JSON, nullable=True)
    last_resource_analyzed_at = Column('last_resource_analyzed_at', TIMESTAMP, nullable=True)
    status_reason = Column('status_reason', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    last_resource_analyzed = Column('last_resource_analyzed', Text, nullable=True)