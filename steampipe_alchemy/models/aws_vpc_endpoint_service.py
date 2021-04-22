from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcEndpointService(Base):
    __tablename__ = 'aws_vpc_endpoint_service'
    service_name = Column('service_name', Text, nullable=True)
    service_id = Column('service_id', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    acceptance_required = Column('acceptance_required', Boolean, nullable=True)
    manages_vpc_endpoints = Column('manages_vpc_endpoints', Boolean, nullable=True)
    private_dns_name = Column('private_dns_name', Text, nullable=True)
    private_dns_name_verification_state = Column('private_dns_name_verification_state', Text, nullable=True)
    vpc_endpoint_policy_supported = Column('vpc_endpoint_policy_supported', Boolean, nullable=True)
    service_type = Column('service_type', JSON, nullable=True)
    base_endpoint_dns_names = Column('base_endpoint_dns_names', JSON, nullable=True)
    availability_zones = Column('availability_zones', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)