from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlobalacceleratorAccelerator(Base, FormatMixins):
    __tablename__ = 'aws_globalaccelerator_accelerator'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    enabled = Column('enabled', Boolean, nullable=True)
    ip_sets = Column('ip_sets', JSON, nullable=True)
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    accelerator_attributes = Column('accelerator_attributes', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    dns_name = Column('dns_name', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    ip_address_type = Column('ip_address_type', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    region = Column('region', Text, nullable=True)