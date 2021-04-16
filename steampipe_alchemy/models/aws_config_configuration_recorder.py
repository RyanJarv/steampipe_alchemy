from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsConfigConfigurationRecorder(Base):
    __tablename__ = 'aws_config_configuration_recorder'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    recording_group = Column(JSON, name='recording_group', nullable=True)
    role_arn = Column(Text, name='role_arn', nullable=True)
    status_recording = Column(Boolean, name='status_recording', nullable=True)
    status = Column(JSON, name='status', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    title = Column(Text, name='title', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)