from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsDynamodbBackup(Base):
    __tablename__ = 'aws_dynamodb_backup'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    table_name = Column('table_name', Text, nullable=True)
    table_arn = Column('table_arn', Text, nullable=True)
    table_id = Column('table_id', Text, nullable=True)
    backup_status = Column('backup_status', Text, nullable=True)
    backup_type = Column('backup_type', Text, nullable=True)
    backup_creation_datetime = Column('backup_creation_datetime', TIMESTAMP, nullable=True)
    backup_expiry_datetime = Column('backup_expiry_datetime', TIMESTAMP, nullable=True)
    backup_size_bytes = Column('backup_size_bytes', BigInteger, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)