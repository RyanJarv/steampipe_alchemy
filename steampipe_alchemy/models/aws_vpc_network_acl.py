from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcNetworkAcl(Base, FormatMixins):
    __tablename__ = 'aws_vpc_network_acl'
    tags = Column('tags', JSON, nullable=True)
    is_default = Column('is_default', Boolean, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    associations = Column('associations', JSON, nullable=True)
    entries = Column('entries', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    network_acl_id = Column('network_acl_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)