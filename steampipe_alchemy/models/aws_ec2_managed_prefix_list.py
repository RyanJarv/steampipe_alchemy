from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2ManagedPrefixList(Base, FormatMixins):
    __tablename__ = 'aws_ec2_managed_prefix_list'
    _ctx = Column('_ctx', JSON, nullable=True)
    max_entries = Column('max_entries', BigInteger, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    state_message = Column('state_message', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    state = Column('state', Text, nullable=True)
    address_family = Column('address_family', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)