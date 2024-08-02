from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCognitoIdentityProvider(Base, FormatMixins):
    __tablename__ = 'aws_cognito_identity_provider'
    _ctx = Column('_ctx', JSON, nullable=True)
    attribute_mapping = Column('attribute_mapping', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    idp_identifiers = Column('idp_identifiers', JSON, nullable=True)
    last_modified_date = Column('last_modified_date', TIMESTAMP, nullable=True)
    provider_details = Column('provider_details', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    provider_name = Column('provider_name', Text, nullable=True)
    user_pool_id = Column('user_pool_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    provider_type = Column('provider_type', Text, nullable=True)