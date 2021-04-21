from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamVirtualMfaDevice(Base):
    __tablename__ = 'aws_iam_virtual_mfa_device'
    serial_number = Column(name='serial_number', type_=Text, nullable=True)
    enable_date = Column(name='enable_date', type_=TIMESTAMP, nullable=True)
    user_id = Column(name='user_id', type_=Text, nullable=True)
    user_name = Column(name='user_name', type_=Text, nullable=True)
    user = Column(name='user', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)