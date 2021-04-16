from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2NetworkLoadBalancer(Base):
    __tablename__ = 'aws_ec2_network_load_balancer'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    type = Column(Text, name='type', nullable=True)
    scheme = Column(Text, name='scheme', nullable=True)
    canonical_hosted_zone_id = Column(Text, name='canonical_hosted_zone_id', nullable=True)
    created_time = Column(TIMESTAMP, name='created_time', nullable=True)
    customer_owned_ipv4_pool = Column(Text, name='customer_owned_ipv4_pool', nullable=True)
    dns_name = Column(Text, name='dns_name', nullable=True)
    ip_address_type = Column(Text, name='ip_address_type', nullable=True)
    state_code = Column(Text, name='state_code', nullable=True)
    state_reason = Column(Text, name='state_reason', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    availability_zones = Column(JSON, name='availability_zones', nullable=True)
    security_groups = Column(JSON, name='security_groups', nullable=True)
    load_balancer_attributes = Column(JSON, name='load_balancer_attributes', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)