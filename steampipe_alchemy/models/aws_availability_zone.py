from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsAvailabilityZone(Base, FormatMixins):
    __tablename__ = 'aws_availability_zone'
    name = Column('name', Text, primary_key=True, nullable=True)
    zone_id = Column('zone_id', Text, nullable=True)
    zone_type = Column('zone_type', Text, nullable=True)
    opt_in_status = Column('opt_in_status', Text, nullable=True)
    group_name = Column('group_name', Text, nullable=True)
    region_name = Column('region_name', Text, nullable=True)
    parent_zone_name = Column('parent_zone_name', Text, nullable=True)
    parent_zone_id = Column('parent_zone_id', Text, nullable=True)
    messages = Column('messages', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)


# Local materialized view table
class AwsAvailabilityZoneLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_availability_zone_local'
    name = Column('name', Text, primary_key=True, nullable=True)
    zone_id = Column('zone_id', Text, nullable=True)
    zone_type = Column('zone_type', Text, nullable=True)
    opt_in_status = Column('opt_in_status', Text, nullable=True)
    group_name = Column('group_name', Text, nullable=True)
    region_name = Column('region_name', Text, nullable=True)
    parent_zone_name = Column('parent_zone_name', Text, nullable=True)
    parent_zone_id = Column('parent_zone_id', Text, nullable=True)
    messages = Column('messages', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)


cache = select(AwsAvailabilityZone).select_from(AwsAvailabilityZone)
create_materialized_view('aws_availability_zone_local', cache, db.metadata_materialized)
