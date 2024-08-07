from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2TargetGroup(Base, FormatMixins):
    __tablename__ = 'aws_ec2_target_group'
    healthy_threshold_count = Column('healthy_threshold_count', BigInteger, nullable=True)
    health_check_timeout_seconds = Column('health_check_timeout_seconds', BigInteger, nullable=True)
    target_health_descriptions = Column('target_health_descriptions', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    unhealthy_threshold_count = Column('unhealthy_threshold_count', BigInteger, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    health_check_enabled = Column('health_check_enabled', Boolean, nullable=True)
    health_check_interval_seconds = Column('health_check_interval_seconds', BigInteger, nullable=True)
    load_balancer_arns = Column('load_balancer_arns', JSON, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    health_check_port = Column('health_check_port', Text, nullable=True)
    target_group_arn = Column('target_group_arn', Text, nullable=True)
    target_type = Column('target_type', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    protocol = Column('protocol', Text, nullable=True)
    matcher_http_code = Column('matcher_http_code', Text, nullable=True)
    matcher_grpc_code = Column('matcher_grpc_code', Text, nullable=True)
    health_check_path = Column('health_check_path', Text, nullable=True)
    target_group_name = Column('target_group_name', Text, nullable=True)
    health_check_protocol = Column('health_check_protocol', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)