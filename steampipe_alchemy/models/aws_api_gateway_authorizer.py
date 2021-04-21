from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayAuthorizer(Base):
    __tablename__ = 'aws_api_gateway_authorizer'
    id = Column(name='id', type_=Text, primary_key=True, nullable=True)
    name = Column(name='name', type_=Text, nullable=True)
    rest_api_id = Column(name='rest_api_id', type_=Text, nullable=True)
    auth_type = Column(name='auth_type', type_=Text, nullable=True)
    authorizer_credentials = Column(name='authorizer_credentials', type_=Text, nullable=True)
    authorizer_uri = Column(name='authorizer_uri', type_=Text, nullable=True)
    identity_validation_expression = Column(name='identity_validation_expression', type_=Text, nullable=True)
    identity_source = Column(name='identity_source', type_=Text, nullable=True)
    provider_arns = Column(name='provider_arns', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)