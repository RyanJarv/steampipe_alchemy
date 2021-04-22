from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcEndpoint(Base):
    __tablename__ = 'aws_vpc_endpoint'
    vpc_endpoint_id = Column('vpc_endpoint_id', Text, nullable=True)
    service_name = Column('service_name', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    private_dns_enabled = Column('private_dns_enabled', Boolean, nullable=True)
    requester_managed = Column('requester_managed', Boolean, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    subnet_ids = Column('subnet_ids', JSON, nullable=True)
    route_table_ids = Column('route_table_ids', JSON, nullable=True)
    groups = Column('groups', JSON, nullable=True)
    network_interface_ids = Column('network_interface_ids', JSON, nullable=True)
    dns_entries = Column('dns_entries', JSON, nullable=True)
    creation_timestamp = Column('creation_timestamp', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)