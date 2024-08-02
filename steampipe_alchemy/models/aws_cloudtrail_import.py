from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudtrailImport(Base, FormatMixins):
    __tablename__ = 'aws_cloudtrail_import'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_timestamp = Column('created_timestamp', TIMESTAMP, nullable=True)
    end_event_time = Column('end_event_time', TIMESTAMP, nullable=True)
    start_event_time = Column('start_event_time', TIMESTAMP, nullable=True)
    updated_timestamp = Column('updated_timestamp', TIMESTAMP, nullable=True)
    destinations = Column('destinations', JSON, nullable=True)
    import_source = Column('import_source', JSON, nullable=True)
    import_statistics = Column('import_statistics', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    import_status = Column('import_status', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    import_id = Column('import_id', Text, nullable=True)