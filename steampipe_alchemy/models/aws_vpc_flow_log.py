from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcFlowLog(Base):
    __tablename__ = 'aws_vpc_flow_log'
    flow_log_id = Column(name='flow_log_id', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    deliver_logs_error_message = Column(name='deliver_logs_error_message', type_=Text, nullable=True)
    deliver_logs_permission_arn = Column(name='deliver_logs_permission_arn', type_=Text, nullable=True)
    deliver_logs_status = Column(name='deliver_logs_status', type_=Text, nullable=True)
    flow_log_status = Column(name='flow_log_status', type_=Text, nullable=True)
    log_group_name = Column(name='log_group_name', type_=Text, nullable=True)
    resource_id = Column(name='resource_id', type_=Text, nullable=True)
    traffic_type = Column(name='traffic_type', type_=Text, nullable=True)
    log_destination_type = Column(name='log_destination_type', type_=Text, nullable=True)
    log_destination = Column(name='log_destination', type_=Text, nullable=True)
    bucket_name = Column(name='bucket_name', type_=Text, nullable=True)
    log_format = Column(name='log_format', type_=Text, nullable=True)
    max_aggregation_interval = Column(name='max_aggregation_interval', type_=BigInteger, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)