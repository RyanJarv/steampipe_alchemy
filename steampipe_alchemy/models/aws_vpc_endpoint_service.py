from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcEndpointService(Base):
    __tablename__ = 'aws_vpc_endpoint_service'
    service_name = Column(name='service_name', type_=Text, nullable=True)
    service_id = Column(name='service_id', type_=Text, nullable=True)
    owner = Column(name='owner', type_=Text, nullable=True)
    acceptance_required = Column(name='acceptance_required', type_=Boolean, nullable=True)
    manages_vpc_endpoints = Column(name='manages_vpc_endpoints', type_=Boolean, nullable=True)
    private_dns_name = Column(name='private_dns_name', type_=Text, nullable=True)
    private_dns_name_verification_state = Column(name='private_dns_name_verification_state', type_=Text, nullable=True)
    vpc_endpoint_policy_supported = Column(name='vpc_endpoint_policy_supported', type_=Boolean, nullable=True)
    service_type = Column(name='service_type', type_=JSON, nullable=True)
    base_endpoint_dns_names = Column(name='base_endpoint_dns_names', type_=JSON, nullable=True)
    availability_zones = Column(name='availability_zones', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)