from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsKinesisVideoStream(Base):
    __tablename__ = 'aws_kinesis_video_stream'
    stream_name = Column(name='stream_name', type_=Text, nullable=True)
    stream_arn = Column(name='stream_arn', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    version = Column(name='version', type_=Text, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    data_retention_in_hours = Column(name='data_retention_in_hours', type_=BigInteger, nullable=True)
    device_name = Column(name='device_name', type_=Text, nullable=True)
    media_type = Column(name='media_type', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)