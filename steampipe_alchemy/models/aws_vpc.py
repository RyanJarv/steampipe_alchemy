from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsVpc(Base, FormatMixins):
    __tablename__ = 'aws_vpc'
    vpc_id = Column('vpc_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cidr_block = Column('cidr_block', psql.CIDR, nullable=True)
    state = Column('state', Text, nullable=True)
    is_default = Column('is_default', Boolean, nullable=True)
    dhcp_options_id = Column('dhcp_options_id', Text, nullable=True)
    instance_tenancy = Column('instance_tenancy', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    cidr_block_association_set = Column('cidr_block_association_set', JSON, nullable=True)
    ipv6_cidr_block_association_set = Column('ipv6_cidr_block_association_set', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsVpcLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_vpc_local'
    vpc_id = Column('vpc_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cidr_block = Column('cidr_block', psql.CIDR, nullable=True)
    state = Column('state', Text, nullable=True)
    is_default = Column('is_default', Boolean, nullable=True)
    dhcp_options_id = Column('dhcp_options_id', Text, nullable=True)
    instance_tenancy = Column('instance_tenancy', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    cidr_block_association_set = Column('cidr_block_association_set', JSON, nullable=True)
    ipv6_cidr_block_association_set = Column('ipv6_cidr_block_association_set', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsVpc).select_from(AwsVpc)
create_materialized_view('aws_vpc_local', cache, db.metadata_materialized)
