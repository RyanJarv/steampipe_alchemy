from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEbsSnapshot(Base):
    __tablename__ = 'aws_ebs_snapshot'
    snapshot_id = Column(Text, name='snapshot_id', nullable=True)
    state = Column(Text, name='state', nullable=True)
    volume_size = Column(BigInteger, name='volume_size', nullable=True)
    volume_id = Column(Text, name='volume_id', nullable=True)
    encrypted = Column(Boolean, name='encrypted', nullable=True)
    start_time = Column(TIMESTAMP, name='start_time', nullable=True)
    description = Column(Text, name='description', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    data_encryption_key_id = Column(Text, name='data_encryption_key_id', nullable=True)
    progress = Column(Text, name='progress', nullable=True)
    state_message = Column(Text, name='state_message', nullable=True)
    owner_alias = Column(Text, name='owner_alias', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    create_volume_permissions = Column(JSON, name='create_volume_permissions', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)