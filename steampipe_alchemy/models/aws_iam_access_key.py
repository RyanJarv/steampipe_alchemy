from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamAccessKey(Base):
    __tablename__ = 'aws_iam_access_key'
    access_key_id = Column(Text, name='access_key_id', nullable=True)
    user_name = Column(Text, name='user_name', nullable=True)
    status = Column(Text, name='status', nullable=True)
    create_date = Column(TIMESTAMP, name='create_date', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)