from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsServerlessapplicationrepositoryApplication(Base, FormatMixins):
    __tablename__ = 'aws_serverlessapplicationrepository_application'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    is_verified_author = Column('is_verified_author', Boolean, nullable=True)
    labels = Column('labels', JSON, nullable=True)
    statements = Column('statements', JSON, nullable=True)
    version = Column('version', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    readme_url = Column('readme_url', Text, nullable=True)
    spdx_license_id = Column('spdx_license_id', Text, nullable=True)
    verified_author_url = Column('verified_author_url', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    author = Column('author', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    home_page_url = Column('home_page_url', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    license_url = Column('license_url', Text, nullable=True)