from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDrsRecoveryInstance(Base, FormatMixins):
    __tablename__ = 'aws_drs_recovery_instance'
    _ctx = Column('_ctx', JSON, nullable=True)
    is_drill = Column('is_drill', Boolean, nullable=True)
    data_replication_info = Column('data_replication_info', JSON, nullable=True)
    failback = Column('failback', JSON, nullable=True)
    recovery_instance_properties = Column('recovery_instance_properties', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    point_in_time_snapshot_date_time = Column('point_in_time_snapshot_date_time', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    source_server_id = Column('source_server_id', Text, nullable=True)
    ec2_instance_id = Column('ec2_instance_id', Text, nullable=True)
    ec2_instance_state = Column('ec2_instance_state', Text, nullable=True)
    recovery_instance_id = Column('recovery_instance_id', Text, nullable=True)
    job_id = Column('job_id', Text, nullable=True)
    origin_environment = Column('origin_environment', Text, nullable=True)