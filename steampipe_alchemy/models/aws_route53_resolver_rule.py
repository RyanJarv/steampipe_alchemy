from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRoute53ResolverRule(Base):
    __tablename__ = 'aws_route53_resolver_rule'
    name = Column(name='name', type_=Text, nullable=True)
    id = Column(name='id', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    creator_request_id = Column(name='creator_request_id', type_=Text, nullable=True)
    domain_name = Column(name='domain_name', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    resolver_endpoint_id = Column(name='resolver_endpoint_id', type_=Text, nullable=True)
    rule_type = Column(name='rule_type', type_=Text, nullable=True)
    share_status = Column(name='share_status', type_=Text, nullable=True)
    status_message = Column(name='status_message', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=Text, nullable=True)
    modification_time = Column(name='modification_time', type_=Text, nullable=True)
    resolver_rule_associations = Column(name='resolver_rule_associations', type_=JSON, nullable=True)
    target_ips = Column(name='target_ips', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)