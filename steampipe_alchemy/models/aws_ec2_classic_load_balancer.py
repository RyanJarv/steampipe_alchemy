from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2ClassicLoadBalancer(Base):
    __tablename__ = 'aws_ec2_classic_load_balancer'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    scheme = Column(name='scheme', type_=Text, nullable=True)
    created_time = Column(name='created_time', type_=TIMESTAMP, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    access_log_emit_interval = Column(name='access_log_emit_interval', type_=BigInteger, nullable=True)
    access_log_enabled = Column(name='access_log_enabled', type_=Boolean, nullable=True)
    access_log_s3_bucket_name = Column(name='access_log_s3_bucket_name', type_=Text, nullable=True)
    access_log_s3_bucket_prefix = Column(name='access_log_s3_bucket_prefix', type_=Text, nullable=True)
    canonical_hosted_zone_name = Column(name='canonical_hosted_zone_name', type_=Text, nullable=True)
    canonical_hosted_zone_name_id = Column(name='canonical_hosted_zone_name_id', type_=Text, nullable=True)
    connection_draining_enabled = Column(name='connection_draining_enabled', type_=Boolean, nullable=True)
    connection_draining_timeout = Column(name='connection_draining_timeout', type_=BigInteger, nullable=True)
    connection_settings_idle_timeout = Column(name='connection_settings_idle_timeout', type_=BigInteger, nullable=True)
    cross_zone_load_balancing_enabled = Column(name='cross_zone_load_balancing_enabled', type_=Boolean, nullable=True)
    dns_name = Column(name='dns_name', type_=Text, nullable=True)
    health_check_interval = Column(name='health_check_interval', type_=BigInteger, nullable=True)
    health_check_timeout = Column(name='health_check_timeout', type_=BigInteger, nullable=True)
    healthy_threshold = Column(name='healthy_threshold', type_=BigInteger, nullable=True)
    heath_check_target = Column(name='heath_check_target', type_=Text, nullable=True)
    source_security_group_name = Column(name='source_security_group_name', type_=Text, nullable=True)
    source_security_group_owner_alias = Column(name='source_security_group_owner_alias', type_=Text, nullable=True)
    unhealthy_threshold = Column(name='unhealthy_threshold', type_=BigInteger, nullable=True)
    additional_attributes = Column(name='additional_attributes', type_=JSON, nullable=True)
    app_cookie_stickiness_policies = Column(name='app_cookie_stickiness_policies', type_=JSON, nullable=True)
    availability_zones = Column(name='availability_zones', type_=JSON, nullable=True)
    backend_server_descriptions = Column(name='backend_server_descriptions', type_=JSON, nullable=True)
    instances = Column(name='instances', type_=JSON, nullable=True)
    lb_cookie_stickiness_policies = Column(name='lb_cookie_stickiness_policies', type_=JSON, nullable=True)
    listener_descriptions = Column(name='listener_descriptions', type_=JSON, nullable=True)
    other_policies = Column(name='other_policies', type_=JSON, nullable=True)
    security_groups = Column(name='security_groups', type_=JSON, nullable=True)
    subnets = Column(name='subnets', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)