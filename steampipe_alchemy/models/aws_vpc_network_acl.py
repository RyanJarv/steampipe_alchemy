from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsVpcNetworkAcl(Base, FormatMixins):
    __tablename__ = 'aws_vpc_network_acl'
    network_acl_id = Column('network_acl_id', Text, nullable=True)
    is_default = Column('is_default', Boolean, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    associations = Column('associations', JSON, nullable=True)
    entries = Column('entries', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsVpcNetworkAclLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_vpc_network_acl_local'
    network_acl_id = Column('network_acl_id', Text, nullable=True)
    is_default = Column('is_default', Boolean, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    associations = Column('associations', JSON, nullable=True)
    entries = Column('entries', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsVpcNetworkAcl).select_from(AwsVpcNetworkAcl)
create_materialized_view('aws_vpc_network_acl_local', cache, db.metadata_materialized)
