from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAvailabilityZone(Base, FormatMixins):
    __tablename__ = 'aws_availability_zone'
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    opt_in_status = Column('opt_in_status', Text, nullable=True)
    group_name = Column('group_name', Text, nullable=True)
    region_name = Column('region_name', Text, nullable=True)
    parent_zone_name = Column('parent_zone_name', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    messages = Column('messages', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    parent_zone_id = Column('parent_zone_id', Text, nullable=True)
    zone_id = Column('zone_id', Text, nullable=True)
    zone_type = Column('zone_type', Text, nullable=True)