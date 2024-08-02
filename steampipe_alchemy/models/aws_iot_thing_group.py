from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIotThingGroup(Base, FormatMixins):
    __tablename__ = 'aws_iot_thing_group'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    attribute_payload = Column('attribute_payload', JSON, nullable=True)
    root_to_parent_thing_groups = Column('root_to_parent_thing_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    query_version = Column('query_version', Text, nullable=True)
    group_name = Column('group_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    thing_group_id = Column('thing_group_id', Text, nullable=True)
    thing_group_description = Column('thing_group_description', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    parent_group_name = Column('parent_group_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    index_name = Column('index_name', Text, nullable=True)
    query_string = Column('query_string', Text, nullable=True)