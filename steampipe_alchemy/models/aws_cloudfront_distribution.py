from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudfrontDistribution(Base, FormatMixins):
    __tablename__ = 'aws_cloudfront_distribution'
    _ctx = Column('_ctx', JSON, nullable=True)
    active_trusted_key_groups = Column('active_trusted_key_groups', JSON, nullable=True)
    active_trusted_signers = Column('active_trusted_signers', JSON, nullable=True)
    aliases = Column('aliases', JSON, nullable=True)
    alias_icp_recordals = Column('alias_icp_recordals', JSON, nullable=True)
    cache_behaviors = Column('cache_behaviors', JSON, nullable=True)
    custom_error_responses = Column('custom_error_responses', JSON, nullable=True)
    default_cache_behavior = Column('default_cache_behavior', JSON, nullable=True)
    logging = Column('logging', JSON, nullable=True)
    origins = Column('origins', JSON, nullable=True)
    origin_groups = Column('origin_groups', JSON, nullable=True)
    restrictions = Column('restrictions', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    viewer_certificate = Column('viewer_certificate', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    enabled = Column('enabled', Boolean, nullable=True)
    is_ipv6_enabled = Column('is_ipv6_enabled', Boolean, nullable=True)
    in_progress_invalidation_batches = Column('in_progress_invalidation_batches', BigInteger, nullable=True)
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    caller_reference = Column('caller_reference', Text, nullable=True)
    comment = Column('comment', Text, nullable=True)
    default_root_object = Column('default_root_object', Text, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    e_tag = Column('e_tag', Text, nullable=True)
    http_version = Column('http_version', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    price_class = Column('price_class', Text, nullable=True)
    web_acl_id = Column('web_acl_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)