from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEfsFileSystem(Base, FormatMixins):
    __tablename__ = 'aws_efs_file_system'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    number_of_mount_targets = Column('number_of_mount_targets', BigInteger, nullable=True)
    encrypted = Column('encrypted', Boolean, nullable=True)
    provisioned_throughput_in_mibps = Column('provisioned_throughput_in_mibps', psql.DOUBLE_PRECISION, nullable=True)
    size_in_bytes = Column('size_in_bytes', JSON, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    throughput_mode = Column('throughput_mode', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    file_system_id = Column('file_system_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    creation_token = Column('creation_token', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    automatic_backups = Column('automatic_backups', Text, nullable=True)
    life_cycle_state = Column('life_cycle_state', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    performance_mode = Column('performance_mode', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)