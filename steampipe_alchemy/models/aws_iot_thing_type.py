from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIotThingType(Base, FormatMixins):
    __tablename__ = 'aws_iot_thing_type'
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    deprecated = Column('deprecated', Boolean, nullable=True)
    deprecation_date = Column('deprecation_date', TIMESTAMP, nullable=True)
    searchable_attributes = Column('searchable_attributes', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    thing_type_id = Column('thing_type_id', Text, nullable=True)
    thing_type_description = Column('thing_type_description', Text, nullable=True)
    thing_type_name = Column('thing_type_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)