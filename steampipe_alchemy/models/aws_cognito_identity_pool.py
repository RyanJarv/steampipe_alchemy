from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCognitoIdentityPool(Base, FormatMixins):
    __tablename__ = 'aws_cognito_identity_pool'
    _ctx = Column('_ctx', JSON, nullable=True)
    allow_unauthenticated_identities = Column('allow_unauthenticated_identities', Boolean, nullable=True)
    allow_classic_flow = Column('allow_classic_flow', Boolean, nullable=True)
    cognito_identity_providers = Column('cognito_identity_providers', JSON, nullable=True)
    open_id_connect_provider_arns = Column('open_id_connect_provider_arns', JSON, nullable=True)
    saml_provider_arns = Column('saml_provider_arns', JSON, nullable=True)
    supported_login_providers = Column('supported_login_providers', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    identity_pool_name = Column('identity_pool_name', Text, nullable=True)
    identity_pool_id = Column('identity_pool_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    developer_provider_name = Column('developer_provider_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)