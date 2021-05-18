from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsConfigConfigurationRecorder(Base, FormatMixins):
    __tablename__ = 'aws_config_configuration_recorder'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    recording_group = Column('recording_group', JSON, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    status_recording = Column('status_recording', Boolean, nullable=True)
    status = Column('status', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsConfigConfigurationRecorderLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_config_configuration_recorder_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    recording_group = Column('recording_group', JSON, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    status_recording = Column('status_recording', Boolean, nullable=True)
    status = Column('status', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsConfigConfigurationRecorder).select_from(AwsConfigConfigurationRecorder)
create_materialized_view('aws_config_configuration_recorder_local', cache, db.metadata_materialized)
