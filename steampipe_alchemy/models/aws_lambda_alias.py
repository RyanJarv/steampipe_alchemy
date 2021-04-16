from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsLambdaAlias(Base):
    __tablename__ = 'aws_lambda_alias'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    function_name = Column(Text, name='function_name', nullable=True)
    alias_arn = Column(Text, name='alias_arn', nullable=True)
    function_version = Column(Text, name='function_version', nullable=True)
    revision_id = Column(Text, name='revision_id', nullable=True)
    description = Column(Text, name='description', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)