from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEbsVolume(Base):
    __tablename__ = 'aws_ebs_volume'
    volume_id = Column(name='volume_id', type_=Text, nullable=True)
    volume_type = Column(name='volume_type', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    create_time = Column(name='create_time', type_=TIMESTAMP, nullable=True)
    auto_enable_io = Column(name='auto_enable_io', type_=Boolean, nullable=True)
    availability_zone = Column(name='availability_zone', type_=Text, nullable=True)
    encrypted = Column(name='encrypted', type_=Boolean, nullable=True)
    fast_restored = Column(name='fast_restored', type_=Boolean, nullable=True)
    iops = Column(name='iops', type_=BigInteger, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    multi_attach_enabled = Column(name='multi_attach_enabled', type_=Boolean, nullable=True)
    outpost_arn = Column(name='outpost_arn', type_=Text, nullable=True)
    size = Column(name='size', type_=BigInteger, nullable=True)
    snapshot_id = Column(name='snapshot_id', type_=Text, nullable=True)
    attachments = Column(name='attachments', type_=JSON, nullable=True)
    product_codes = Column(name='product_codes', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)