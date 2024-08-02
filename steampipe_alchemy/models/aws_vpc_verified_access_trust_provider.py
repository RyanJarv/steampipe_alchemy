from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcVerifiedAccessTrustProvider(Base, FormatMixins):
    __tablename__ = 'aws_vpc_verified_access_trust_provider'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    last_updated_time = Column('last_updated_time', TIMESTAMP, nullable=True)
    oidc_options = Column('oidc_options', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    user_trust_provider_type = Column('user_trust_provider_type', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    verified_access_trust_provider_id = Column('verified_access_trust_provider_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    device_trust_provider_type = Column('device_trust_provider_type', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    policy_reference_name = Column('policy_reference_name', Text, nullable=True)
    trust_provider_type = Column('trust_provider_type', Text, nullable=True)