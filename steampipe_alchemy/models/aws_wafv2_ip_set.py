from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWafv2IpSet(Base, FormatMixins):
    __tablename__ = 'aws_wafv2_ip_set'
    tags_src = Column('tags_src', JSON, nullable=True)
    addresses = Column('addresses', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    lock_token = Column('lock_token', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    id = Column('id', Text, nullable=True)
    scope = Column('scope', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    ip_address_version = Column('ip_address_version', Text, nullable=True)