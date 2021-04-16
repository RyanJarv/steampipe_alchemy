from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsGlacierVault(Base):
    __tablename__ = 'aws_glacier_vault'
    vault_name = Column(Text, name='vault_name', nullable=True)
    vault_arn = Column(Text, name='vault_arn', nullable=True)
    creation_date = Column(TIMESTAMP, name='creation_date', nullable=True)
    last_inventory_date = Column(TIMESTAMP, name='last_inventory_date', nullable=True)
    number_of_archives = Column(BigInteger, name='number_of_archives', nullable=True)
    size_in_bytes = Column(BigInteger, name='size_in_bytes', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    vault_lock_policy = Column(JSON, name='vault_lock_policy', nullable=True)
    vault_lock_policy_std = Column(JSON, name='vault_lock_policy_std', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)