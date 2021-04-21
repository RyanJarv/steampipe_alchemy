from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsAvailabilityZone(Base):
    __tablename__ = 'aws_availability_zone'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    zone_id = Column(name='zone_id', type_=Text, nullable=True)
    zone_type = Column(name='zone_type', type_=Text, nullable=True)
    opt_in_status = Column(name='opt_in_status', type_=Text, nullable=True)
    group_name = Column(name='group_name', type_=Text, nullable=True)
    region_name = Column(name='region_name', type_=Text, nullable=True)
    parent_zone_name = Column(name='parent_zone_name', type_=Text, nullable=True)
    parent_zone_id = Column(name='parent_zone_id', type_=Text, nullable=True)
    messages = Column(name='messages', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)