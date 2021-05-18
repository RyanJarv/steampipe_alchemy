from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsGlacierVault(Base, FormatMixins):
    __tablename__ = 'aws_glacier_vault'
    vault_name = Column('vault_name', Text, nullable=True)
    vault_arn = Column('vault_arn', Text, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    last_inventory_date = Column('last_inventory_date', TIMESTAMP, nullable=True)
    number_of_archives = Column('number_of_archives', BigInteger, nullable=True)
    size_in_bytes = Column('size_in_bytes', BigInteger, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    vault_lock_policy = Column('vault_lock_policy', JSON, nullable=True)
    vault_lock_policy_std = Column('vault_lock_policy_std', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsGlacierVaultLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_glacier_vault_local'
    vault_name = Column('vault_name', Text, nullable=True)
    vault_arn = Column('vault_arn', Text, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    last_inventory_date = Column('last_inventory_date', TIMESTAMP, nullable=True)
    number_of_archives = Column('number_of_archives', BigInteger, nullable=True)
    size_in_bytes = Column('size_in_bytes', BigInteger, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    vault_lock_policy = Column('vault_lock_policy', JSON, nullable=True)
    vault_lock_policy_std = Column('vault_lock_policy_std', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsGlacierVault).select_from(AwsGlacierVault)
create_materialized_view('aws_glacier_vault_local', cache, db.metadata_materialized)
