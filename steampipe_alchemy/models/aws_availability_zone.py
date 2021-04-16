from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsAvailabilityZone(Base):
    __tablename__ = 'aws_availability_zone'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    zone_id = Column(Text, name='zone_id', nullable=True)
    zone_type = Column(Text, name='zone_type', nullable=True)
    opt_in_status = Column(Text, name='opt_in_status', nullable=True)
    group_name = Column(Text, name='group_name', nullable=True)
    region_name = Column(Text, name='region_name', nullable=True)
    parent_zone_name = Column(Text, name='parent_zone_name', nullable=True)
    parent_zone_id = Column(Text, name='parent_zone_id', nullable=True)
    messages = Column(Text, name='messages', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)