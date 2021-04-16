from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsKinesisVideoStream(Base):
    __tablename__ = 'aws_kinesis_video_stream'
    stream_name = Column(Text, name='stream_name', nullable=True)
    stream_arn = Column(Text, name='stream_arn', nullable=True)
    status = Column(Text, name='status', nullable=True)
    version = Column(Text, name='version', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    data_retention_in_hours = Column(BigInteger, name='data_retention_in_hours', nullable=True)
    device_name = Column(Text, name='device_name', nullable=True)
    media_type = Column(Text, name='media_type', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)