from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsBackupFramework(Base, FormatMixins):
    __tablename__ = 'aws_backup_framework'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    number_of_controls = Column('number_of_controls', BigInteger, nullable=True)
    framework_controls = Column('framework_controls', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    framework_name = Column('framework_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    framework_description = Column('framework_description', Text, nullable=True)
    deployment_status = Column('deployment_status', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    framework_status = Column('framework_status', Text, nullable=True)