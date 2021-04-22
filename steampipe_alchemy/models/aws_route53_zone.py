from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRoute53Zone(Base):
    __tablename__ = 'aws_route53_zone'
    name = Column('name', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    caller_reference = Column('caller_reference', Text, nullable=True)
    comment = Column('comment', Text, nullable=True)
    private_zone = Column('private_zone', Boolean, nullable=True)
    linked_service_principal = Column('linked_service_principal', Text, nullable=True)
    linked_service_description = Column('linked_service_description', Text, nullable=True)
    resource_record_set_count = Column('resource_record_set_count', BigInteger, nullable=True)
    query_logging_configs = Column('query_logging_configs', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)