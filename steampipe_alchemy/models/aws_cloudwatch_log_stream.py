from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsCloudwatchLogStream(Base):
    __tablename__ = 'aws_cloudwatch_log_stream'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    log_group_name = Column(Text, name='log_group_name', nullable=True)
    creation_time = Column(TIMESTAMP, name='creation_time', nullable=True)
    first_event_timestamp = Column(TIMESTAMP, name='first_event_timestamp', nullable=True)
    last_event_timestamp = Column(TIMESTAMP, name='last_event_timestamp', nullable=True)
    last_ingestion_time = Column(TIMESTAMP, name='last_ingestion_time', nullable=True)
    upload_sequence_token = Column(Text, name='upload_sequence_token', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)