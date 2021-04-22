from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2ApplicationLoadBalancer(Base):
    __tablename__ = 'aws_ec2_application_load_balancer'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    type = Column('type', Text, nullable=True)
    scheme = Column('scheme', Text, nullable=True)
    canonical_hosted_zone_id = Column('canonical_hosted_zone_id', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    customer_owned_ipv4_pool = Column('customer_owned_ipv4_pool', Text, nullable=True)
    dns_name = Column('dns_name', Text, nullable=True)
    ip_address_type = Column('ip_address_type', Text, nullable=True)
    state_code = Column('state_code', Text, nullable=True)
    state_reason = Column('state_reason', Text, nullable=True)
    availability_zones = Column('availability_zones', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    load_balancer_attributes = Column('load_balancer_attributes', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)