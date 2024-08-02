from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEfsMountTarget(Base, FormatMixins):
    __tablename__ = 'aws_efs_mount_target'
    ip_address = Column('ip_address', psql.INET, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    network_interface_id = Column('network_interface_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    subnet_id = Column('subnet_id', Text, nullable=True)
    mount_target_id = Column('mount_target_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    file_system_id = Column('file_system_id', Text, nullable=True)
    life_cycle_state = Column('life_cycle_state', Text, nullable=True)
    availability_zone_id = Column('availability_zone_id', Text, nullable=True)
    availability_zone_name = Column('availability_zone_name', Text, nullable=True)