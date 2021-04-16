from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRoute53ResolverRule(Base):
    __tablename__ = 'aws_route53_resolver_rule'
    name = Column(Text, name='name', nullable=True)
    id = Column(Text, name='id', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    status = Column(Text, name='status', nullable=True)
    creator_request_id = Column(Text, name='creator_request_id', nullable=True)
    domain_name = Column(Text, name='domain_name', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    resolver_endpoint_id = Column(Text, name='resolver_endpoint_id', nullable=True)
    rule_type = Column(Text, name='rule_type', nullable=True)
    share_status = Column(Text, name='share_status', nullable=True)
    status_message = Column(Text, name='status_message', nullable=True)
    creation_time = Column(Text, name='creation_time', nullable=True)
    modification_time = Column(Text, name='modification_time', nullable=True)
    resolver_rule_associations = Column(JSON, name='resolver_rule_associations', nullable=True)
    target_ips = Column(JSON, name='target_ips', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)