from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsCloudwatchLogStream(Base):
    __tablename__ = 'aws_cloudwatch_log_stream'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    log_group_name = Column('log_group_name', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    first_event_timestamp = Column('first_event_timestamp', TIMESTAMP, nullable=True)
    last_event_timestamp = Column('last_event_timestamp', TIMESTAMP, nullable=True)
    last_ingestion_time = Column('last_ingestion_time', TIMESTAMP, nullable=True)
    upload_sequence_token = Column('upload_sequence_token', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)