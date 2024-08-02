from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsS3BucketIntelligentTieringConfiguration(Base, FormatMixins):
    __tablename__ = 'aws_s3_bucket_intelligent_tiering_configuration'
    filter = Column('filter', JSON, nullable=True)
    tierings = Column('tierings', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    bucket_name = Column('bucket_name', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    title = Column('title', Text, nullable=True)