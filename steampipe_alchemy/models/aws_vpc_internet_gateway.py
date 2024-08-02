from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcInternetGateway(Base, FormatMixins):
    __tablename__ = 'aws_vpc_internet_gateway'
    _ctx = Column('_ctx', JSON, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    internet_gateway_id = Column('internet_gateway_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)