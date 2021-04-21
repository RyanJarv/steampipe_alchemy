from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamAccessKey(Base):
    __tablename__ = 'aws_iam_access_key'
    access_key_id = Column(name='access_key_id', type_=Text, nullable=True)
    user_name = Column(name='user_name', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    create_date = Column(name='create_date', type_=TIMESTAMP, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)