from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsKmsKeyRotation(Base, FormatMixins):
    __tablename__ = 'aws_kms_key_rotation'
    rotation_date = Column('rotation_date', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    key_id = Column('key_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    key_arn = Column('key_arn', Text, nullable=True)
    rotation_type = Column('rotation_type', Text, nullable=True)