from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53Zone(Base, FormatMixins):
    __tablename__ = 'aws_route53_zone'
    _ctx = Column('_ctx', JSON, nullable=True)
    private_zone = Column('private_zone', Boolean, nullable=True)
    resource_record_set_count = Column('resource_record_set_count', BigInteger, nullable=True)
    query_logging_configs = Column('query_logging_configs', JSON, nullable=True)
    dnssec_key_signing_keys = Column('dnssec_key_signing_keys', JSON, nullable=True)
    dnssec_status = Column('dnssec_status', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    vpcs = Column('vpcs', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    resource_record_set_limit = Column('resource_record_set_limit', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    caller_reference = Column('caller_reference', Text, nullable=True)
    comment = Column('comment', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    linked_service_principal = Column('linked_service_principal', Text, nullable=True)
    linked_service_description = Column('linked_service_description', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)