from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsIamAccessKey(Base, FormatMixins):
    __tablename__ = 'aws_iam_access_key'
    access_key_id = Column('access_key_id', Text, nullable=True)
    user_name = Column('user_name', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsIamAccessKeyLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_iam_access_key_local'
    access_key_id = Column('access_key_id', Text, nullable=True)
    user_name = Column('user_name', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsIamAccessKey).select_from(AwsIamAccessKey)
create_materialized_view('aws_iam_access_key_local', cache, db.metadata_materialized)
