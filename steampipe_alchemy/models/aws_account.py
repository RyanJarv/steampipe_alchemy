from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsAccount(Base):
    __tablename__ = 'aws_account'
    account_aliases = Column(JSON, name='account_aliases', nullable=True)
    organization_id = Column(Text, name='organization_id', nullable=True)
    organization_arn = Column(Text, name='organization_arn', nullable=True)
    organization_feature_set = Column(Text, name='organization_feature_set', nullable=True)
    organization_master_account_arn = Column(Text, name='organization_master_account_arn', nullable=True)
    organization_master_account_email = Column(Text, name='organization_master_account_email', nullable=True)
    organization_master_account_id = Column(Text, name='organization_master_account_id', nullable=True)
    organization_available_policy_types = Column(JSON, name='organization_available_policy_types', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)