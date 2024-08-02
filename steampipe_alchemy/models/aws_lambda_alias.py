from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsLambdaAlias(Base, FormatMixins):
    __tablename__ = 'aws_lambda_alias'
    _ctx = Column('_ctx', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    url_config = Column('url_config', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    function_name = Column('function_name', Text, nullable=True)
    alias_arn = Column('alias_arn', Text, nullable=True)
    function_version = Column('function_version', Text, nullable=True)
    revision_id = Column('revision_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)