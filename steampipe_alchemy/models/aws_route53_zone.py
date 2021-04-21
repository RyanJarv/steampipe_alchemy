from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRoute53Zone(Base):
    __tablename__ = 'aws_route53_zone'
    name = Column(name='name', type_=Text, nullable=True)
    id = Column(name='id', type_=Text, primary_key=True, nullable=True)
    caller_reference = Column(name='caller_reference', type_=Text, nullable=True)
    comment = Column(name='comment', type_=Text, nullable=True)
    private_zone = Column(name='private_zone', type_=Boolean, nullable=True)
    linked_service_principal = Column(name='linked_service_principal', type_=Text, nullable=True)
    linked_service_description = Column(name='linked_service_description', type_=Text, nullable=True)
    resource_record_set_count = Column(name='resource_record_set_count', type_=BigInteger, nullable=True)
    query_logging_configs = Column(name='query_logging_configs', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)