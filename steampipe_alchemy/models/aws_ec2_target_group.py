from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2TargetGroup(Base):
    __tablename__ = 'aws_ec2_target_group'
    target_group_name = Column(Text, name='target_group_name', nullable=True)
    target_group_arn = Column(Text, name='target_group_arn', nullable=True)
    target_type = Column(Text, name='target_type', nullable=True)
    load_balancer_arns = Column(JSON, name='load_balancer_arns', nullable=True)
    port = Column(BigInteger, name='port', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    protocol = Column(Text, name='protocol', nullable=True)
    matcher_http_code = Column(Text, name='matcher_http_code', nullable=True)
    matcher_grpc_code = Column(Text, name='matcher_grpc_code', nullable=True)
    healthy_threshold_count = Column(BigInteger, name='healthy_threshold_count', nullable=True)
    unhealthy_threshold_count = Column(BigInteger, name='unhealthy_threshold_count', nullable=True)
    health_check_enabled = Column(Boolean, name='health_check_enabled', nullable=True)
    health_check_interval_seconds = Column(BigInteger, name='health_check_interval_seconds', nullable=True)
    health_check_path = Column(Text, name='health_check_path', nullable=True)
    health_check_port = Column(Text, name='health_check_port', nullable=True)
    health_check_protocol = Column(Text, name='health_check_protocol', nullable=True)
    health_check_timeout_seconds = Column(BigInteger, name='health_check_timeout_seconds', nullable=True)
    target_health_descriptions = Column(JSON, name='target_health_descriptions', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)