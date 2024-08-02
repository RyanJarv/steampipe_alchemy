from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDynamodbTableExport(Base, FormatMixins):
    __tablename__ = 'aws_dynamodb_table_export'
    end_time = Column('end_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    item_count = Column('item_count', BigInteger, nullable=True)
    export_time = Column('export_time', TIMESTAMP, nullable=True)
    start_time = Column('start_time', TIMESTAMP, nullable=True)
    billed_size_bytes = Column('billed_size_bytes', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    s3_bucket_owner = Column('s3_bucket_owner', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    s3_sse_algorithm = Column('s3_sse_algorithm', Text, nullable=True)
    s3_sse_kms_key_id = Column('s3_sse_kms_key_id', Text, nullable=True)
    table_arn = Column('table_arn', Text, nullable=True)
    table_id = Column('table_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    s3_prefix = Column('s3_prefix', Text, nullable=True)
    export_status = Column('export_status', Text, nullable=True)
    client_token = Column('client_token', Text, nullable=True)
    export_format = Column('export_format', Text, nullable=True)
    export_manifest = Column('export_manifest', Text, nullable=True)
    failure_code = Column('failure_code', Text, nullable=True)
    failure_message = Column('failure_message', Text, nullable=True)
    s3_bucket = Column('s3_bucket', Text, nullable=True)