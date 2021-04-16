from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRoute53Zone(Base):
    __tablename__ = 'aws_route53_zone'
    name = Column(Text, name='name', nullable=True)
    id = Column(Text, name='id', primary_key=True, nullable=True)
    caller_reference = Column(Text, name='caller_reference', nullable=True)
    comment = Column(Text, name='comment', nullable=True)
    private_zone = Column(Boolean, name='private_zone', nullable=True)
    linked_service_principal = Column(Text, name='linked_service_principal', nullable=True)
    linked_service_description = Column(Text, name='linked_service_description', nullable=True)
    resource_record_set_count = Column(BigInteger, name='resource_record_set_count', nullable=True)
    query_logging_configs = Column(JSON, name='query_logging_configs', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)