from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamVirtualMfaDevice(Base, FormatMixins):
    __tablename__ = 'aws_iam_virtual_mfa_device'
    akas = Column('akas', JSON, nullable=True)
    user = Column('user', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    enable_date = Column('enable_date', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    assignment_status = Column('assignment_status', Text, nullable=True)
    user_id = Column('user_id', Text, nullable=True)
    user_name = Column('user_name', Text, nullable=True)
    serial_number = Column('serial_number', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)