from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlueSecurityConfiguration(Base, FormatMixins):
    __tablename__ = 'aws_glue_security_configuration'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_time_stamp = Column('created_time_stamp', TIMESTAMP, nullable=True)
    cloud_watch_encryption = Column('cloud_watch_encryption', JSON, nullable=True)
    job_bookmarks_encryption = Column('job_bookmarks_encryption', JSON, nullable=True)
    s3_encryption = Column('s3_encryption', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)