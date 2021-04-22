from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsDynamodbTable(Base):
    __tablename__ = 'aws_dynamodb_table'
    name = Column('name', Text, primary_key=True, nullable=True)
    table_arn = Column('table_arn', Text, nullable=True)
    table_id = Column('table_id', Text, nullable=True)
    creation_date_time = Column('creation_date_time', TIMESTAMP, nullable=True)
    table_status = Column('table_status', Text, nullable=True)
    billing_mode = Column('billing_mode', Text, nullable=True)
    item_count = Column('item_count', BigInteger, nullable=True)
    global_table_version = Column('global_table_version', Text, nullable=True)
    read_capacity = Column('read_capacity', BigInteger, nullable=True)
    write_capacity = Column('write_capacity', BigInteger, nullable=True)
    latest_stream_arn = Column('latest_stream_arn', Text, nullable=True)
    latest_stream_label = Column('latest_stream_label', Text, nullable=True)
    table_size_bytes = Column('table_size_bytes', BigInteger, nullable=True)
    archival_summary = Column('archival_summary', JSON, nullable=True)
    attribute_definitions = Column('attribute_definitions', JSON, nullable=True)
    key_schema = Column('key_schema', JSON, nullable=True)
    sse_description = Column('sse_description', JSON, nullable=True)
    continuous_backups_status = Column('continuous_backups_status', Text, nullable=True)
    point_in_time_recovery_description = Column('point_in_time_recovery_description', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)