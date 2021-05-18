from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsAccessanalyzerAnalyzer(Base, FormatMixins):
    __tablename__ = 'aws_accessanalyzer_analyzer'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    last_resource_analyzed = Column('last_resource_analyzed', Text, nullable=True)
    last_resource_analyzed_at = Column('last_resource_analyzed_at', TIMESTAMP, nullable=True)
    status_reason = Column('status_reason', Text, nullable=True)
    findings = Column('findings', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsAccessanalyzerAnalyzerLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_accessanalyzer_analyzer_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    last_resource_analyzed = Column('last_resource_analyzed', Text, nullable=True)
    last_resource_analyzed_at = Column('last_resource_analyzed_at', TIMESTAMP, nullable=True)
    status_reason = Column('status_reason', Text, nullable=True)
    findings = Column('findings', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsAccessanalyzerAnalyzer).select_from(AwsAccessanalyzerAnalyzer)
create_materialized_view('aws_accessanalyzer_analyzer_local', cache, db.metadata_materialized)
