from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsConfigConfigurationRecorder(Base, FormatMixins):
    __tablename__ = 'aws_config_configuration_recorder'
    recording_group = Column('recording_group', JSON, nullable=True)
    status_recording = Column('status_recording', Boolean, nullable=True)
    status = Column('status', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    title = Column('title', Text, nullable=True)