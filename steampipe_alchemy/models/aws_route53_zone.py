from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsRoute53Zone(Base, FormatMixins):
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


# Local materialized view table
class AwsRoute53ZoneLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_route53_zone_local'
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


cache = select(AwsRoute53Zone).select_from(AwsRoute53Zone)
create_materialized_view('aws_route53_zone_local', cache, db.metadata_materialized)
