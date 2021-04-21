from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsGlacierVault(Base):
    __tablename__ = 'aws_glacier_vault'
    vault_name = Column(name='vault_name', type_=Text, nullable=True)
    vault_arn = Column(name='vault_arn', type_=Text, nullable=True)
    creation_date = Column(name='creation_date', type_=TIMESTAMP, nullable=True)
    last_inventory_date = Column(name='last_inventory_date', type_=TIMESTAMP, nullable=True)
    number_of_archives = Column(name='number_of_archives', type_=BigInteger, nullable=True)
    size_in_bytes = Column(name='size_in_bytes', type_=BigInteger, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    vault_lock_policy = Column(name='vault_lock_policy', type_=JSON, nullable=True)
    vault_lock_policy_std = Column(name='vault_lock_policy_std', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)