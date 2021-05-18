from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsRoute53ResolverRule(Base, FormatMixins):
    __tablename__ = 'aws_route53_resolver_rule'
    name = Column('name', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    creator_request_id = Column('creator_request_id', Text, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    resolver_endpoint_id = Column('resolver_endpoint_id', Text, nullable=True)
    rule_type = Column('rule_type', Text, nullable=True)
    share_status = Column('share_status', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    creation_time = Column('creation_time', Text, nullable=True)
    modification_time = Column('modification_time', Text, nullable=True)
    resolver_rule_associations = Column('resolver_rule_associations', JSON, nullable=True)
    target_ips = Column('target_ips', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsRoute53ResolverRuleLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_route53_resolver_rule_local'
    name = Column('name', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    creator_request_id = Column('creator_request_id', Text, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    resolver_endpoint_id = Column('resolver_endpoint_id', Text, nullable=True)
    rule_type = Column('rule_type', Text, nullable=True)
    share_status = Column('share_status', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    creation_time = Column('creation_time', Text, nullable=True)
    modification_time = Column('modification_time', Text, nullable=True)
    resolver_rule_associations = Column('resolver_rule_associations', JSON, nullable=True)
    target_ips = Column('target_ips', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsRoute53ResolverRule).select_from(AwsRoute53ResolverRule)
create_materialized_view('aws_route53_resolver_rule_local', cache, db.metadata_materialized)
