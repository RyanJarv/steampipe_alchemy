from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsVpcEgressOnlyInternetGateway(Base, FormatMixins):
    __tablename__ = 'aws_vpc_egress_only_internet_gateway'
    id = Column('id', Text, primary_key=True, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsVpcEgressOnlyInternetGatewayLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_vpc_egress_only_internet_gateway_local'
    id = Column('id', Text, primary_key=True, nullable=True)
    attachments = Column('attachments', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsVpcEgressOnlyInternetGateway).select_from(AwsVpcEgressOnlyInternetGateway)
create_materialized_view('aws_vpc_egress_only_internet_gateway_local', cache, db.metadata_materialized)
