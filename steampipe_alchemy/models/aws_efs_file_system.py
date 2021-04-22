from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEfsFileSystem(Base):
    __tablename__ = 'aws_efs_file_system'
    name = Column('name', Text, primary_key=True, nullable=True)
    file_system_id = Column('file_system_id', Text, nullable=True)
    file_system_arn = Column('file_system_arn', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    creation_token = Column('creation_token', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    life_cycle_state = Column('life_cycle_state', Text, nullable=True)
    number_of_mount_targets = Column('number_of_mount_targets', BigInteger, nullable=True)
    performance_mode = Column('performance_mode', Text, nullable=True)
    encrypted = Column('encrypted', Boolean, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    throughput_mode = Column('throughput_mode', Text, nullable=True)
    provisioned_throughput_in_mibps = Column('provisioned_throughput_in_mibps', psql.DOUBLE_PRECISION, nullable=True)
    size_in_bytes = Column('size_in_bytes', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)