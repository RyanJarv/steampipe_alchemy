from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcFlowLog(Base):
    __tablename__ = 'aws_vpc_flow_log'
    flow_log_id = Column(Text, name='flow_log_id', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    deliver_logs_error_message = Column(Text, name='deliver_logs_error_message', nullable=True)
    deliver_logs_permission_arn = Column(Text, name='deliver_logs_permission_arn', nullable=True)
    deliver_logs_status = Column(Text, name='deliver_logs_status', nullable=True)
    flow_log_status = Column(Text, name='flow_log_status', nullable=True)
    log_group_name = Column(Text, name='log_group_name', nullable=True)
    resource_id = Column(Text, name='resource_id', nullable=True)
    traffic_type = Column(Text, name='traffic_type', nullable=True)
    log_destination_type = Column(Text, name='log_destination_type', nullable=True)
    log_destination = Column(Text, name='log_destination', nullable=True)
    bucket_name = Column(Text, name='bucket_name', nullable=True)
    log_format = Column(Text, name='log_format', nullable=True)
    max_aggregation_interval = Column(BigInteger, name='max_aggregation_interval', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)