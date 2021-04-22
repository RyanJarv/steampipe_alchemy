from steampipe_alchemy.types.aws_vpc_route_table import *

from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcRouteTable(Base):
    __tablename__ = 'aws_vpc_route_table'
    route_table_id = Column('route_table_id', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    associations: Associations = Column('associations', JSON, nullable=True)
    routes: Routes = Column('routes', JSON, nullable=True)
    propagating_vgws: PropagatingVgws = Column('propagating_vgws', JSON, nullable=True)
    tags_src: TagsSrc = Column('tags_src', JSON, nullable=True)
    tags: Tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas: Akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)