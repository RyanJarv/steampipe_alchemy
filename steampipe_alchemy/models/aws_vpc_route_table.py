from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcRouteTable(Base, FormatMixins):
    __tablename__ = 'aws_vpc_route_table'
    associations = Column('associations', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    routes = Column('routes', JSON, nullable=True)
    propagating_vgws = Column('propagating_vgws', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    route_table_id = Column('route_table_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)