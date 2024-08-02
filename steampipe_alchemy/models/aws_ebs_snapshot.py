from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEbsSnapshot(Base, FormatMixins):
    __tablename__ = 'aws_ebs_snapshot'
    encrypted = Column('encrypted', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    start_time = Column('start_time', TIMESTAMP, nullable=True)
    volume_size = Column('volume_size', BigInteger, nullable=True)
    create_volume_permissions = Column('create_volume_permissions', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    snapshot_id = Column('snapshot_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    owner_alias = Column('owner_alias', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    state = Column('state', Text, nullable=True)
    volume_id = Column('volume_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    data_encryption_key_id = Column('data_encryption_key_id', Text, nullable=True)
    progress = Column('progress', Text, nullable=True)
    state_message = Column('state_message', Text, nullable=True)