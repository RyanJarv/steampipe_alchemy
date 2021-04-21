from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudwatchLogStream(Base):
    __tablename__ = 'aws_cloudwatch_log_stream'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    log_group_name = Column(name='log_group_name', type_=Text, nullable=True)
    creation_time = Column(name='creation_time', type_=TIMESTAMP, nullable=True)
    first_event_timestamp = Column(name='first_event_timestamp', type_=TIMESTAMP, nullable=True)
    last_event_timestamp = Column(name='last_event_timestamp', type_=TIMESTAMP, nullable=True)
    last_ingestion_time = Column(name='last_ingestion_time', type_=TIMESTAMP, nullable=True)
    upload_sequence_token = Column(name='upload_sequence_token', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)