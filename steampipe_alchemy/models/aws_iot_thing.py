from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIotThing(Base, FormatMixins):
    __tablename__ = 'aws_iot_thing'
    _ctx = Column('_ctx', JSON, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    attributes = Column('attributes', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    attribute_value = Column('attribute_value', Text, nullable=True)
    billing_group_name = Column('billing_group_name', Text, nullable=True)
    default_client_id = Column('default_client_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    thing_name = Column('thing_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    thing_id = Column('thing_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    thing_type_name = Column('thing_type_name', Text, nullable=True)
    attribute_name = Column('attribute_name', Text, nullable=True)