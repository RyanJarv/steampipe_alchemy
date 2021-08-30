from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcNatGateway(Base, FormatMixins):
    __tablename__ = 'aws_vpc_nat_gateway'
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    delete_time = Column('delete_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    nat_gateway_addresses = Column('nat_gateway_addresses', JSON, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    provisioned_bandwidth = Column('provisioned_bandwidth', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    nat_gateway_id = Column('nat_gateway_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    state = Column('state', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    subnet_id = Column('subnet_id', Text, nullable=True)
    failure_code = Column('failure_code', Text, nullable=True)
    failure_message = Column('failure_message', Text, nullable=True)