from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsKmsKey(Base):
    __tablename__ = 'aws_kms_key'
    id = Column(Text, name='id', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    key_manager = Column(Text, name='key_manager', nullable=True)
    creation_date = Column(TIMESTAMP, name='creation_date', nullable=True)
    aws_account_id = Column(Text, name='aws_account_id', nullable=True)
    enabled = Column(Boolean, name='enabled', nullable=True)
    customer_master_key_spec = Column(Text, name='customer_master_key_spec', nullable=True)
    description = Column(Text, name='description', nullable=True)
    deletion_date = Column(TIMESTAMP, name='deletion_date', nullable=True)
    key_state = Column(Text, name='key_state', nullable=True)
    key_usage = Column(Text, name='key_usage', nullable=True)
    origin = Column(Text, name='origin', nullable=True)
    valid_to = Column(TIMESTAMP, name='valid_to', nullable=True)
    aliases = Column(JSON, name='aliases', nullable=True)
    key_rotation_enabled = Column(Boolean, name='key_rotation_enabled', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)