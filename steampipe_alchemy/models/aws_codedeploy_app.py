from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCodedeployApp(Base, FormatMixins):
    __tablename__ = 'aws_codedeploy_app'
    _ctx = Column('_ctx', JSON, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    linked_to_github = Column('linked_to_github', Boolean, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    application_id = Column('application_id', Text, nullable=True)
    application_name = Column('application_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    compute_platform = Column('compute_platform', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    github_account_name = Column('github_account_name', Text, nullable=True)
    region = Column('region', Text, nullable=True)