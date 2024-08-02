from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodepipelinePipeline(Base, FormatMixins):
    __tablename__ = 'aws_codepipeline_pipeline'
    _ctx = Column('_ctx', JSON, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    encryption_key = Column('encryption_key', JSON, nullable=True)
    artifact_stores = Column('artifact_stores', JSON, nullable=True)
    stages = Column('stages', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)