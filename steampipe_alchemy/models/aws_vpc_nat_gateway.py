from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcNatGateway(Base):
    __tablename__ = 'aws_vpc_nat_gateway'
    nat_gateway_id = Column(Text, name='nat_gateway_id', nullable=True)
    nat_gateway_addresses = Column(JSON, name='nat_gateway_addresses', nullable=True)
    state = Column(Text, name='state', nullable=True)
    create_time = Column(TIMESTAMP, name='create_time', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    subnet_id = Column(Text, name='subnet_id', nullable=True)
    delete_time = Column(TIMESTAMP, name='delete_time', nullable=True)
    failure_code = Column(Text, name='failure_code', nullable=True)
    failure_message = Column(Text, name='failure_message', nullable=True)
    provisioned_bandwidth = Column(JSON, name='provisioned_bandwidth', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)