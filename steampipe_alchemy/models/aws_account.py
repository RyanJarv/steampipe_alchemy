from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsAccount(Base):
    __tablename__ = 'aws_account'
    account_aliases = Column(name='account_aliases', type_=JSON, nullable=True)
    organization_id = Column(name='organization_id', type_=Text, nullable=True)
    organization_arn = Column(name='organization_arn', type_=Text, nullable=True)
    organization_feature_set = Column(name='organization_feature_set', type_=Text, nullable=True)
    organization_master_account_arn = Column(name='organization_master_account_arn', type_=Text, nullable=True)
    organization_master_account_email = Column(name='organization_master_account_email', type_=Text, nullable=True)
    organization_master_account_id = Column(name='organization_master_account_id', type_=Text, nullable=True)
    organization_available_policy_types = Column(name='organization_available_policy_types', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)