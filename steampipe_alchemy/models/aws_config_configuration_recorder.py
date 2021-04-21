from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsConfigConfigurationRecorder(Base):
    __tablename__ = 'aws_config_configuration_recorder'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    recording_group = Column(name='recording_group', type_=JSON, nullable=True)
    role_arn = Column(name='role_arn', type_=Text, nullable=True)
    status_recording = Column(name='status_recording', type_=Boolean, nullable=True)
    status = Column(name='status', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)