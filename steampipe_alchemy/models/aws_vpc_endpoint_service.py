from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcEndpointService(Base):
    __tablename__ = 'aws_vpc_endpoint_service'
    service_name = Column(Text, name='service_name', nullable=True)
    service_id = Column(Text, name='service_id', nullable=True)
    owner = Column(Text, name='owner', nullable=True)
    acceptance_required = Column(Boolean, name='acceptance_required', nullable=True)
    manages_vpc_endpoints = Column(Boolean, name='manages_vpc_endpoints', nullable=True)
    private_dns_name = Column(Text, name='private_dns_name', nullable=True)
    private_dns_name_verification_state = Column(Text, name='private_dns_name_verification_state', nullable=True)
    vpc_endpoint_policy_supported = Column(Boolean, name='vpc_endpoint_policy_supported', nullable=True)
    service_type = Column(JSON, name='service_type', nullable=True)
    base_endpoint_dns_names = Column(JSON, name='base_endpoint_dns_names', nullable=True)
    availability_zones = Column(JSON, name='availability_zones', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)