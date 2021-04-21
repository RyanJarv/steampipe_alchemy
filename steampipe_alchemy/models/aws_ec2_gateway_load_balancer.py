from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2GatewayLoadBalancer(Base):
    __tablename__ = 'aws_ec2_gateway_load_balancer'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    state_code = Column(name='state_code', type_=Text, nullable=True)
    scheme = Column(name='scheme', type_=Text, nullable=True)
    dns_name = Column(name='dns_name', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    created_time = Column(name='created_time', type_=TIMESTAMP, nullable=True)
    ip_address_type = Column(name='ip_address_type', type_=Text, nullable=True)
    availability_zones = Column(name='availability_zones', type_=JSON, nullable=True)
    canonical_hosted_zone_id = Column(name='canonical_hosted_zone_id', type_=Text, nullable=True)
    customer_owned_ipv4_pool = Column(name='customer_owned_ipv4_pool', type_=Text, nullable=True)
    security_groups = Column(name='security_groups', type_=JSON, nullable=True)
    load_balancer_attributes = Column(name='load_balancer_attributes', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)