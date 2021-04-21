from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsKmsKey(Base):
    __tablename__ = 'aws_kms_key'
    id = Column(name='id', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    key_manager = Column(name='key_manager', type_=Text, nullable=True)
    creation_date = Column(name='creation_date', type_=TIMESTAMP, nullable=True)
    aws_account_id = Column(name='aws_account_id', type_=Text, nullable=True)
    enabled = Column(name='enabled', type_=Boolean, nullable=True)
    customer_master_key_spec = Column(name='customer_master_key_spec', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    deletion_date = Column(name='deletion_date', type_=TIMESTAMP, nullable=True)
    key_state = Column(name='key_state', type_=Text, nullable=True)
    key_usage = Column(name='key_usage', type_=Text, nullable=True)
    origin = Column(name='origin', type_=Text, nullable=True)
    valid_to = Column(name='valid_to', type_=TIMESTAMP, nullable=True)
    aliases = Column(name='aliases', type_=JSON, nullable=True)
    key_rotation_enabled = Column(name='key_rotation_enabled', type_=Boolean, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)