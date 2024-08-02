from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcPeeringConnection(Base, FormatMixins):
    __tablename__ = 'aws_vpc_peering_connection'
    _ctx = Column('_ctx', JSON, nullable=True)
    accepter_cidr_block = Column('accepter_cidr_block', psql.CIDR, nullable=True)
    expiration_time = Column('expiration_time', TIMESTAMP, nullable=True)
    requester_cidr_block = Column('requester_cidr_block', psql.CIDR, nullable=True)
    accepter_cidr_block_set = Column('accepter_cidr_block_set', JSON, nullable=True)
    accepter_ipv6_cidr_block_set = Column('accepter_ipv6_cidr_block_set', JSON, nullable=True)
    accepter_peering_options = Column('accepter_peering_options', JSON, nullable=True)
    requester_cidr_block_set = Column('requester_cidr_block_set', JSON, nullable=True)
    requester_ipv6_cidr_block_set = Column('requester_ipv6_cidr_block_set', JSON, nullable=True)
    requester_peering_options = Column('requester_peering_options', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    status_code = Column('status_code', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    accepter_owner_id = Column('accepter_owner_id', Text, nullable=True)
    accepter_region = Column('accepter_region', Text, nullable=True)
    accepter_vpc_id = Column('accepter_vpc_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    requester_owner_id = Column('requester_owner_id', Text, nullable=True)
    requester_region = Column('requester_region', Text, nullable=True)
    requester_vpc_id = Column('requester_vpc_id', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)