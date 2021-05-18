from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsAccount(Base, FormatMixins):
    __tablename__ = 'aws_account'
    account_aliases = Column('account_aliases', JSON, nullable=True)
    organization_id = Column('organization_id', Text, nullable=True)
    organization_arn = Column('organization_arn', Text, nullable=True)
    organization_feature_set = Column('organization_feature_set', Text, nullable=True)
    organization_master_account_arn = Column('organization_master_account_arn', Text, nullable=True)
    organization_master_account_email = Column('organization_master_account_email', Text, nullable=True)
    organization_master_account_id = Column('organization_master_account_id', Text, nullable=True)
    organization_available_policy_types = Column('organization_available_policy_types', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsAccountLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_account_local'
    account_aliases = Column('account_aliases', JSON, nullable=True)
    organization_id = Column('organization_id', Text, nullable=True)
    organization_arn = Column('organization_arn', Text, nullable=True)
    organization_feature_set = Column('organization_feature_set', Text, nullable=True)
    organization_master_account_arn = Column('organization_master_account_arn', Text, nullable=True)
    organization_master_account_email = Column('organization_master_account_email', Text, nullable=True)
    organization_master_account_id = Column('organization_master_account_id', Text, nullable=True)
    organization_available_policy_types = Column('organization_available_policy_types', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsAccount).select_from(AwsAccount)
create_materialized_view('aws_account_local', cache, db.metadata_materialized)
