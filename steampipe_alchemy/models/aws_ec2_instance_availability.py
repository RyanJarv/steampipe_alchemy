from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2InstanceAvailability(Base):
    __tablename__ = 'aws_ec2_instance_availability'
    instance_type = Column(name='instance_type', type_=Text, nullable=True)
    location = Column(name='location', type_=Text, nullable=True)
    location_type = Column(name='location_type', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)