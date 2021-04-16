from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsDynamodbBackup(Base):
    __tablename__ = 'aws_dynamodb_backup'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    table_name = Column(Text, name='table_name', nullable=True)
    table_arn = Column(Text, name='table_arn', nullable=True)
    table_id = Column(Text, name='table_id', nullable=True)
    backup_status = Column(Text, name='backup_status', nullable=True)
    backup_type = Column(Text, name='backup_type', nullable=True)
    backup_creation_datetime = Column(TIMESTAMP, name='backup_creation_datetime', nullable=True)
    backup_expiry_datetime = Column(TIMESTAMP, name='backup_expiry_datetime', nullable=True)
    backup_size_bytes = Column(BigInteger, name='backup_size_bytes', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)