from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2TargetGroup(Base):
    __tablename__ = 'aws_ec2_target_group'
    target_group_name = Column(name='target_group_name', type_=Text, nullable=True)
    target_group_arn = Column(name='target_group_arn', type_=Text, nullable=True)
    target_type = Column(name='target_type', type_=Text, nullable=True)
    load_balancer_arns = Column(name='load_balancer_arns', type_=JSON, nullable=True)
    port = Column(name='port', type_=BigInteger, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    protocol = Column(name='protocol', type_=Text, nullable=True)
    matcher_http_code = Column(name='matcher_http_code', type_=Text, nullable=True)
    matcher_grpc_code = Column(name='matcher_grpc_code', type_=Text, nullable=True)
    healthy_threshold_count = Column(name='healthy_threshold_count', type_=BigInteger, nullable=True)
    unhealthy_threshold_count = Column(name='unhealthy_threshold_count', type_=BigInteger, nullable=True)
    health_check_enabled = Column(name='health_check_enabled', type_=Boolean, nullable=True)
    health_check_interval_seconds = Column(name='health_check_interval_seconds', type_=BigInteger, nullable=True)
    health_check_path = Column(name='health_check_path', type_=Text, nullable=True)
    health_check_port = Column(name='health_check_port', type_=Text, nullable=True)
    health_check_protocol = Column(name='health_check_protocol', type_=Text, nullable=True)
    health_check_timeout_seconds = Column(name='health_check_timeout_seconds', type_=BigInteger, nullable=True)
    target_health_descriptions = Column(name='target_health_descriptions', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)