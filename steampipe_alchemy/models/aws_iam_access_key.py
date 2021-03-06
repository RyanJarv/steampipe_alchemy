from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamAccessKey(Base, FormatMixins):
    __tablename__ = 'aws_iam_access_key'
    akas = Column('akas', JSON, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    status = Column('status', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    access_key_id = Column('access_key_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    user_name = Column('user_name', Text, nullable=True)