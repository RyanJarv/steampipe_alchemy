from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsBackupProtectedResource(Base, FormatMixins):
    __tablename__ = 'aws_backup_protected_resource'
    last_backup_time = Column('last_backup_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    resource_arn = Column('resource_arn', Text, primary_key=True, nullable=True)