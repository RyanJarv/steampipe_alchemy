from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamVirtualMfaDevice(Base):
    __tablename__ = 'aws_iam_virtual_mfa_device'
    serial_number = Column(Text, name='serial_number', nullable=True)
    enable_date = Column(TIMESTAMP, name='enable_date', nullable=True)
    user_id = Column(Text, name='user_id', nullable=True)
    user_name = Column(Text, name='user_name', nullable=True)
    user = Column(JSON, name='user', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)