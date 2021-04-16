from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEfsFileSystem(Base):
    __tablename__ = 'aws_efs_file_system'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    file_system_id = Column(Text, name='file_system_id', nullable=True)
    file_system_arn = Column(Text, name='file_system_arn', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    creation_token = Column(Text, name='creation_token', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    life_cycle_state = Column(Text, name='life_cycle_state', nullable=True)
    number_of_mount_targets = Column(BigInteger, name='number_of_mount_targets', nullable=True)
    performance_mode = Column(Text, name='performance_mode', nullable=True)
    encrypted = Column(Boolean, name='encrypted', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    throughput_mode = Column(Text, name='throughput_mode', nullable=True)
    provisioned_throughput_in_mibps = Column(psql.DOUBLE_PRECISION, name='provisioned_throughput_in_mibps', nullable=True)
    size_in_bytes = Column(JSON, name='size_in_bytes', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)