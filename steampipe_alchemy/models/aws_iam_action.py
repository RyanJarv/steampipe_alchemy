from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsIamAction(Base):
    __tablename__ = 'aws_iam_action'
    action = Column('action', Text, primary_key=True, nullable=True)
    prefix = Column('prefix', Text, nullable=True)
    privilege = Column('privilege', Text, nullable=True)
    access_level = Column('access_level', Text, nullable=True)
    description = Column('description', Text, nullable=True)