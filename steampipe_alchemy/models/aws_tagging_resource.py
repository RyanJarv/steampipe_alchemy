from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsTaggingResource(Base, FormatMixins):
    __tablename__ = 'aws_tagging_resource'
    _ctx = Column('_ctx', JSON, nullable=True)
    compliance_status = Column('compliance_status', Boolean, nullable=True)
    keys_with_noncompliant_values = Column('keys_with_noncompliant_values', JSON, nullable=True)
    noncompliant_keys = Column('noncompliant_keys', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)