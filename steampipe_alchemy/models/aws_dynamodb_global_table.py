from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsDynamodbGlobalTable(Base):
    __tablename__ = 'aws_dynamodb_global_table'
    global_table_name = Column('global_table_name', Text, nullable=True)
    global_table_arn = Column('global_table_arn', Text, nullable=True)
    global_table_status = Column('global_table_status', Text, nullable=True)
    creation_date_time = Column('creation_date_time', TIMESTAMP, nullable=True)
    replication_group = Column('replication_group', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)