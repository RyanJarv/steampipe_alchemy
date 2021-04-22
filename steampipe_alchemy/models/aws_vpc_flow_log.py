from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcFlowLog(Base):
    __tablename__ = 'aws_vpc_flow_log'
    flow_log_id = Column('flow_log_id', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    deliver_logs_error_message = Column('deliver_logs_error_message', Text, nullable=True)
    deliver_logs_permission_arn = Column('deliver_logs_permission_arn', Text, nullable=True)
    deliver_logs_status = Column('deliver_logs_status', Text, nullable=True)
    flow_log_status = Column('flow_log_status', Text, nullable=True)
    log_group_name = Column('log_group_name', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)
    traffic_type = Column('traffic_type', Text, nullable=True)
    log_destination_type = Column('log_destination_type', Text, nullable=True)
    log_destination = Column('log_destination', Text, nullable=True)
    bucket_name = Column('bucket_name', Text, nullable=True)
    log_format = Column('log_format', Text, nullable=True)
    max_aggregation_interval = Column('max_aggregation_interval', BigInteger, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)