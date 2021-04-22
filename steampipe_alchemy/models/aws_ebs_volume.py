from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEbsVolume(Base):
    __tablename__ = 'aws_ebs_volume'
    volume_id = Column('volume_id', Text, nullable=True)
    volume_type = Column('volume_type', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    auto_enable_io = Column('auto_enable_io', Boolean, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    encrypted = Column('encrypted', Boolean, nullable=True)
    fast_restored = Column('fast_restored', Boolean, nullable=True)
    iops = Column('iops', BigInteger, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    multi_attach_enabled = Column('multi_attach_enabled', Boolean, nullable=True)
    outpost_arn = Column('outpost_arn', Text, nullable=True)
    size = Column('size', BigInteger, nullable=True)
    snapshot_id = Column('snapshot_id', Text, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    product_codes = Column('product_codes', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)