from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEbsVolume(Base):
    __tablename__ = 'aws_ebs_volume'
    volume_id = Column(Text, name='volume_id', nullable=True)
    volume_type = Column(Text, name='volume_type', nullable=True)
    state = Column(Text, name='state', nullable=True)
    create_time = Column(TIMESTAMP, name='create_time', nullable=True)
    auto_enable_io = Column(Boolean, name='auto_enable_io', nullable=True)
    availability_zone = Column(Text, name='availability_zone', nullable=True)
    encrypted = Column(Boolean, name='encrypted', nullable=True)
    fast_restored = Column(Boolean, name='fast_restored', nullable=True)
    iops = Column(BigInteger, name='iops', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    multi_attach_enabled = Column(Boolean, name='multi_attach_enabled', nullable=True)
    outpost_arn = Column(Text, name='outpost_arn', nullable=True)
    size = Column(BigInteger, name='size', nullable=True)
    snapshot_id = Column(Text, name='snapshot_id', nullable=True)
    attachments = Column(JSON, name='attachments', nullable=True)
    product_codes = Column(JSON, name='product_codes', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)