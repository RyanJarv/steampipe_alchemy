from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcEndpoint(Base):
    __tablename__ = 'aws_vpc_endpoint'
    vpc_endpoint_id = Column(name='vpc_endpoint_id', type_=Text, nullable=True)
    service_name = Column(name='service_name', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    private_dns_enabled = Column(name='private_dns_enabled', type_=Boolean, nullable=True)
    requester_managed = Column(name='requester_managed', type_=Boolean, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    subnet_ids = Column(name='subnet_ids', type_=JSON, nullable=True)
    route_table_ids = Column(name='route_table_ids', type_=JSON, nullable=True)
    groups = Column(name='groups', type_=JSON, nullable=True)
    network_interface_ids = Column(name='network_interface_ids', type_=JSON, nullable=True)
    dns_entries = Column(name='dns_entries', type_=JSON, nullable=True)
    creation_timestamp = Column(name='creation_timestamp', type_=TIMESTAMP, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)