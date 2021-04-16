from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsDynamodbGlobalTable(Base):
    __tablename__ = 'aws_dynamodb_global_table'
    global_table_name = Column(Text, name='global_table_name', nullable=True)
    global_table_arn = Column(Text, name='global_table_arn', nullable=True)
    global_table_status = Column(Text, name='global_table_status', nullable=True)
    creation_date_time = Column(TIMESTAMP, name='creation_date_time', nullable=True)
    replication_group = Column(JSON, name='replication_group', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)