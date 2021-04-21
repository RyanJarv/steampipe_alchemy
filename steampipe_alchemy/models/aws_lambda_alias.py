from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsLambdaAlias(Base):
    __tablename__ = 'aws_lambda_alias'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    function_name = Column(name='function_name', type_=Text, nullable=True)
    alias_arn = Column(name='alias_arn', type_=Text, nullable=True)
    function_version = Column(name='function_version', type_=Text, nullable=True)
    revision_id = Column(name='revision_id', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)