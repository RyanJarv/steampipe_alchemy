from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcEndpoint(Base):
    __tablename__ = 'aws_vpc_endpoint'
    vpc_endpoint_id = Column(Text, name='vpc_endpoint_id', nullable=True)
    service_name = Column(Text, name='service_name', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    state = Column(Text, name='state', nullable=True)
    private_dns_enabled = Column(Boolean, name='private_dns_enabled', nullable=True)
    requester_managed = Column(Boolean, name='requester_managed', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    subnet_ids = Column(JSON, name='subnet_ids', nullable=True)
    route_table_ids = Column(JSON, name='route_table_ids', nullable=True)
    groups = Column(JSON, name='groups', nullable=True)
    network_interface_ids = Column(JSON, name='network_interface_ids', nullable=True)
    dns_entries = Column(JSON, name='dns_entries', nullable=True)
    creation_timestamp = Column(TIMESTAMP, name='creation_timestamp', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)