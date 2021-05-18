from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsEc2InstanceAvailability(Base, FormatMixins):
    __tablename__ = 'aws_ec2_instance_availability'
    instance_type = Column('instance_type', Text, nullable=True)
    location = Column('location', Text, nullable=True)
    location_type = Column('location_type', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)


# Local materialized view table
class AwsEc2InstanceAvailabilityLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_ec2_instance_availability_local'
    instance_type = Column('instance_type', Text, nullable=True)
    location = Column('location', Text, nullable=True)
    location_type = Column('location_type', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)


cache = select(AwsEc2InstanceAvailability).select_from(AwsEc2InstanceAvailability)
create_materialized_view('aws_ec2_instance_availability_local', cache, db.metadata_materialized)
