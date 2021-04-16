from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsApiGatewayAuthorizer(Base):
    __tablename__ = 'aws_api_gateway_authorizer'
    id = Column(Text, name='id', primary_key=True, nullable=True)
    name = Column(Text, name='name', nullable=True)
    rest_api_id = Column(Text, name='rest_api_id', nullable=True)
    auth_type = Column(Text, name='auth_type', nullable=True)
    authorizer_credentials = Column(Text, name='authorizer_credentials', nullable=True)
    authorizer_uri = Column(Text, name='authorizer_uri', nullable=True)
    identity_validation_expression = Column(Text, name='identity_validation_expression', nullable=True)
    identity_source = Column(Text, name='identity_source', nullable=True)
    provider_arns = Column(JSON, name='provider_arns', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)