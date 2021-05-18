from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsVpcNatGateway(Base, FormatMixins):
    __tablename__ = 'aws_vpc_nat_gateway'
    nat_gateway_id = Column('nat_gateway_id', Text, nullable=True)
    nat_gateway_addresses = Column('nat_gateway_addresses', JSON, nullable=True)
    state = Column('state', Text, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    subnet_id = Column('subnet_id', Text, nullable=True)
    delete_time = Column('delete_time', TIMESTAMP, nullable=True)
    failure_code = Column('failure_code', Text, nullable=True)
    failure_message = Column('failure_message', Text, nullable=True)
    provisioned_bandwidth = Column('provisioned_bandwidth', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsVpcNatGatewayLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_vpc_nat_gateway_local'
    nat_gateway_id = Column('nat_gateway_id', Text, nullable=True)
    nat_gateway_addresses = Column('nat_gateway_addresses', JSON, nullable=True)
    state = Column('state', Text, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    subnet_id = Column('subnet_id', Text, nullable=True)
    delete_time = Column('delete_time', TIMESTAMP, nullable=True)
    failure_code = Column('failure_code', Text, nullable=True)
    failure_message = Column('failure_message', Text, nullable=True)
    provisioned_bandwidth = Column('provisioned_bandwidth', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsVpcNatGateway).select_from(AwsVpcNatGateway)
create_materialized_view('aws_vpc_nat_gateway_local', cache, db.metadata_materialized)
