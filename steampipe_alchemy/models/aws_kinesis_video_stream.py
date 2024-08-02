from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsKinesisVideoStream(Base, FormatMixins):
    __tablename__ = 'aws_kinesis_video_stream'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    data_retention_in_hours = Column('data_retention_in_hours', BigInteger, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    device_name = Column('device_name', Text, nullable=True)
    media_type = Column('media_type', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    stream_name = Column('stream_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    stream_arn = Column('stream_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    version = Column('version', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)