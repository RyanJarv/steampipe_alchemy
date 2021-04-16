from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsDynamodbTable(Base):
    __tablename__ = 'aws_dynamodb_table'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    table_arn = Column(Text, name='table_arn', nullable=True)
    table_id = Column(Text, name='table_id', nullable=True)
    creation_date_time = Column(TIMESTAMP, name='creation_date_time', nullable=True)
    table_status = Column(Text, name='table_status', nullable=True)
    billing_mode = Column(Text, name='billing_mode', nullable=True)
    item_count = Column(BigInteger, name='item_count', nullable=True)
    global_table_version = Column(Text, name='global_table_version', nullable=True)
    read_capacity = Column(BigInteger, name='read_capacity', nullable=True)
    write_capacity = Column(BigInteger, name='write_capacity', nullable=True)
    latest_stream_arn = Column(Text, name='latest_stream_arn', nullable=True)
    latest_stream_label = Column(Text, name='latest_stream_label', nullable=True)
    table_size_bytes = Column(BigInteger, name='table_size_bytes', nullable=True)
    archival_summary = Column(JSON, name='archival_summary', nullable=True)
    attribute_definitions = Column(JSON, name='attribute_definitions', nullable=True)
    key_schema = Column(JSON, name='key_schema', nullable=True)
    sse_description = Column(JSON, name='sse_description', nullable=True)
    continuous_backups_status = Column(Text, name='continuous_backups_status', nullable=True)
    point_in_time_recovery_description = Column(JSON, name='point_in_time_recovery_description', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)