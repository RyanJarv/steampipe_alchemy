from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsmInventoryEntry(Base, FormatMixins):
    __tablename__ = 'aws_ssm_inventory_entry'
    entries = Column('entries', JSON, nullable=True)
    capture_time = Column('capture_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    instance_id = Column('instance_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    type_name = Column('type_name', Text, nullable=True)
    schema_version = Column('schema_version', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)