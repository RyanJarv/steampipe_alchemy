from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsDynamodbGlobalTable(Base, FormatMixins):
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


# Local materialized view table
class AwsDynamodbGlobalTableLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_dynamodb_global_table_local'
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


cache = select(AwsDynamodbGlobalTable).select_from(AwsDynamodbGlobalTable)
create_materialized_view('aws_dynamodb_global_table_local', cache, db.metadata_materialized)
