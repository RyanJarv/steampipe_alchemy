from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEfsFileSystem(Base):
    __tablename__ = 'aws_efs_file_system'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    file_system_id = Column(name='file_system_id', type_=Text, nullable=True)
    file_system_arn = Column(name='file_system_arn', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    creation_token = Column(name='creation_token', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    life_cycle_state = Column(name='life_cycle_state', type_=Text, nullable=True)
    number_of_mount_targets = Column(name='number_of_mount_targets', type_=BigInteger, nullable=True)
    performance_mode = Column(name='performance_mode', type_=Text, nullable=True)
    encrypted = Column(name='encrypted', type_=Boolean, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    throughput_mode = Column(name='throughput_mode', type_=Text, nullable=True)
    provisioned_throughput_in_mibps = Column(name='provisioned_throughput_in_mibps', type_=psql.DOUBLE_PRECISION, nullable=True)
    size_in_bytes = Column(name='size_in_bytes', type_=JSON, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)