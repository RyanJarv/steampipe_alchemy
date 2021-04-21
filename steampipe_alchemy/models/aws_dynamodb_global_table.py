from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsDynamodbGlobalTable(Base):
    __tablename__ = 'aws_dynamodb_global_table'
    global_table_name = Column(name='global_table_name', type_=Text, nullable=True)
    global_table_arn = Column(name='global_table_arn', type_=Text, nullable=True)
    global_table_status = Column(name='global_table_status', type_=Text, nullable=True)
    creation_date_time = Column(name='creation_date_time', type_=TIMESTAMP, nullable=True)
    replication_group = Column(name='replication_group', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)