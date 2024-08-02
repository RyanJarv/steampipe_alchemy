from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDrsSourceServer(Base, FormatMixins):
    __tablename__ = 'aws_drs_source_server'
    data_replication_info = Column('data_replication_info', JSON, nullable=True)
    source_properties = Column('source_properties', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    source_cloud_properties = Column('source_cloud_properties', JSON, nullable=True)
    staging_area = Column('staging_area', JSON, nullable=True)
    life_cycle = Column('life_cycle', JSON, nullable=True)
    launch_configuration = Column('launch_configuration', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    staging_account_id = Column('staging_account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    recovery_instance_id = Column('recovery_instance_id', Text, nullable=True)
    last_launch_result = Column('last_launch_result', Text, nullable=True)
    replication_direction = Column('replication_direction', Text, nullable=True)
    reversed_direction_source_server_arn = Column('reversed_direction_source_server_arn', Text, nullable=True)
    source_server_id = Column('source_server_id', Text, nullable=True)
    hardware_id = Column('hardware_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)