from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEksIdentityProviderConfig(Base, FormatMixins):
    __tablename__ = 'aws_eks_identity_provider_config'
    akas = Column('akas', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    required_claims = Column('required_claims', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    groups_claim = Column('groups_claim', Text, nullable=True)
    groups_prefix = Column('groups_prefix', Text, nullable=True)
    issuer_url = Column('issuer_url', Text, nullable=True)
    username_claim = Column('username_claim', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    username_prefix = Column('username_prefix', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    client_id = Column('client_id', Text, nullable=True)
    cluster_name = Column('cluster_name', Text, nullable=True)