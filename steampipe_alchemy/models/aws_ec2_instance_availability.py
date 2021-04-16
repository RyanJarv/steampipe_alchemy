from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2InstanceAvailability(Base):
    __tablename__ = 'aws_ec2_instance_availability'
    instance_type = Column(Text, name='instance_type', nullable=True)
    location = Column(Text, name='location', nullable=True)
    location_type = Column(Text, name='location_type', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)