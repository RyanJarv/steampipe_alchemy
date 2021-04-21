from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEbsSnapshot(Base):
    __tablename__ = 'aws_ebs_snapshot'
    snapshot_id = Column(name='snapshot_id', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    volume_size = Column(name='volume_size', type_=BigInteger, nullable=True)
    volume_id = Column(name='volume_id', type_=Text, nullable=True)
    encrypted = Column(name='encrypted', type_=Boolean, nullable=True)
    start_time = Column(name='start_time', type_=TIMESTAMP, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    data_encryption_key_id = Column(name='data_encryption_key_id', type_=Text, nullable=True)
    progress = Column(name='progress', type_=Text, nullable=True)
    state_message = Column(name='state_message', type_=Text, nullable=True)
    owner_alias = Column(name='owner_alias', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    create_volume_permissions = Column(name='create_volume_permissions', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)