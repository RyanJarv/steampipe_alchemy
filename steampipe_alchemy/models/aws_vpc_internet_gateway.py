from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsVpcInternetGateway(Base, FormatMixins):
    __tablename__ = 'aws_vpc_internet_gateway'
    internet_gateway_id = Column('internet_gateway_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsVpcInternetGatewayLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_vpc_internet_gateway_local'
    internet_gateway_id = Column('internet_gateway_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsVpcInternetGateway).select_from(AwsVpcInternetGateway)
create_materialized_view('aws_vpc_internet_gateway_local', cache, db.metadata_materialized)
