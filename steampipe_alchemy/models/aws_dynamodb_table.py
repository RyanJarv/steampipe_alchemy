from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsDynamodbTable(Base):
    __tablename__ = 'aws_dynamodb_table'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    table_arn = Column(name='table_arn', type_=Text, nullable=True)
    table_id = Column(name='table_id', type_=Text, nullable=True)
    creation_date_time = Column(name='creation_date_time', type_=TIMESTAMP, nullable=True)
    table_status = Column(name='table_status', type_=Text, nullable=True)
    billing_mode = Column(name='billing_mode', type_=Text, nullable=True)
    item_count = Column(name='item_count', type_=BigInteger, nullable=True)
    global_table_version = Column(name='global_table_version', type_=Text, nullable=True)
    read_capacity = Column(name='read_capacity', type_=BigInteger, nullable=True)
    write_capacity = Column(name='write_capacity', type_=BigInteger, nullable=True)
    latest_stream_arn = Column(name='latest_stream_arn', type_=Text, nullable=True)
    latest_stream_label = Column(name='latest_stream_label', type_=Text, nullable=True)
    table_size_bytes = Column(name='table_size_bytes', type_=BigInteger, nullable=True)
    archival_summary = Column(name='archival_summary', type_=JSON, nullable=True)
    attribute_definitions = Column(name='attribute_definitions', type_=JSON, nullable=True)
    key_schema = Column(name='key_schema', type_=JSON, nullable=True)
    sse_description = Column(name='sse_description', type_=JSON, nullable=True)
    continuous_backups_status = Column(name='continuous_backups_status', type_=Text, nullable=True)
    point_in_time_recovery_description = Column(name='point_in_time_recovery_description', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)