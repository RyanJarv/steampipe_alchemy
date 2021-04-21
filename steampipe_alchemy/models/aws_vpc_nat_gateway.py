from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcNatGateway(Base):
    __tablename__ = 'aws_vpc_nat_gateway'
    nat_gateway_id = Column(name='nat_gateway_id', type_=Text, nullable=True)
    nat_gateway_addresses = Column(name='nat_gateway_addresses', type_=JSON, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    create_time = Column(name='create_time', type_=TIMESTAMP, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    subnet_id = Column(name='subnet_id', type_=Text, nullable=True)
    delete_time = Column(name='delete_time', type_=TIMESTAMP, nullable=True)
    failure_code = Column(name='failure_code', type_=Text, nullable=True)
    failure_message = Column(name='failure_message', type_=Text, nullable=True)
    provisioned_bandwidth = Column(name='provisioned_bandwidth', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)