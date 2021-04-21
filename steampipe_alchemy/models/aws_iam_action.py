from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamAction(Base):
    __tablename__ = 'aws_iam_action'
    action = Column(name='action', type_=Text, primary_key=True, nullable=True)
    prefix = Column(name='prefix', type_=Text, nullable=True)
    privilege = Column(name='privilege', type_=Text, nullable=True)
    access_level = Column(name='access_level', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)