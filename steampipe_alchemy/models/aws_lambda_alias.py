from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsLambdaAlias(Base, FormatMixins):
    __tablename__ = 'aws_lambda_alias'
    name = Column('name', Text, primary_key=True, nullable=True)
    function_name = Column('function_name', Text, nullable=True)
    alias_arn = Column('alias_arn', Text, nullable=True)
    function_version = Column('function_version', Text, nullable=True)
    revision_id = Column('revision_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)