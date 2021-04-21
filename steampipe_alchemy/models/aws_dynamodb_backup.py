from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsDynamodbBackup(Base):
    __tablename__ = 'aws_dynamodb_backup'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    table_name = Column(name='table_name', type_=Text, nullable=True)
    table_arn = Column(name='table_arn', type_=Text, nullable=True)
    table_id = Column(name='table_id', type_=Text, nullable=True)
    backup_status = Column(name='backup_status', type_=Text, nullable=True)
    backup_type = Column(name='backup_type', type_=Text, nullable=True)
    backup_creation_datetime = Column(name='backup_creation_datetime', type_=TIMESTAMP, nullable=True)
    backup_expiry_datetime = Column(name='backup_expiry_datetime', type_=TIMESTAMP, nullable=True)
    backup_size_bytes = Column(name='backup_size_bytes', type_=BigInteger, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)