from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsIamVirtualMfaDevice(Base, FormatMixins):
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


# Local materialized view table
class AwsIamVirtualMfaDeviceLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_iam_virtual_mfa_device_local'
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


cache = select(AwsIamVirtualMfaDevice).select_from(AwsIamVirtualMfaDevice)
create_materialized_view('aws_iam_virtual_mfa_device_local', cache, db.metadata_materialized)
