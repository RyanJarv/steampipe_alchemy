from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDaxSubnetGroup(Base, FormatMixins):
    __tablename__ = 'aws_dax_subnet_group'
    subnets = Column('subnets', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    subnet_group_name = Column('subnet_group_name', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)