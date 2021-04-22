from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamVirtualMfaDevice(Base):
    __tablename__ = 'aws_iam_virtual_mfa_device'
    serial_number = Column('serial_number', Text, nullable=True)
    enable_date = Column('enable_date', TIMESTAMP, nullable=True)
    user_id = Column('user_id', Text, nullable=True)
    user_name = Column('user_name', Text, nullable=True)
    user = Column('user', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)