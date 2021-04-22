from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayAuthorizer(Base):
    __tablename__ = 'aws_api_gateway_authorizer'
    id = Column('id', Text, primary_key=True, nullable=True)
    name = Column('name', Text, nullable=True)
    rest_api_id = Column('rest_api_id', Text, nullable=True)
    auth_type = Column('auth_type', Text, nullable=True)
    authorizer_credentials = Column('authorizer_credentials', Text, nullable=True)
    authorizer_uri = Column('authorizer_uri', Text, nullable=True)
    identity_validation_expression = Column('identity_validation_expression', Text, nullable=True)
    identity_source = Column('identity_source', Text, nullable=True)
    provider_arns = Column('provider_arns', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)