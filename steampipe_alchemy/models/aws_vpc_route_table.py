from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcRouteTable(Base):
    __tablename__ = 'aws_vpc_route_table'
    route_table_id = Column(name='route_table_id', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    associations = Column(name='associations', type_=JSON, nullable=True)
    routes = Column(name='routes', type_=JSON, nullable=True)
    propagating_vgws = Column(name='propagating_vgws', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)