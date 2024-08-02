from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamServiceSpecificCredential(Base, FormatMixins):
    __tablename__ = 'aws_iam_service_specific_credential'
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    status = Column('status', Text, nullable=True)
    user_name = Column('user_name', Text, nullable=True)
    service_name = Column('service_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    service_specific_credential_id = Column('service_specific_credential_id', Text, nullable=True)
    service_user_name = Column('service_user_name', Text, nullable=True)