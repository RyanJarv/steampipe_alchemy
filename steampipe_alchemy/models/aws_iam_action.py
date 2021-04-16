from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsIamAction(Base):
    __tablename__ = 'aws_iam_action'
    action = Column(Text, name='action', primary_key=True, nullable=True)
    prefix = Column(Text, name='prefix', nullable=True)
    privilege = Column(Text, name='privilege', nullable=True)
    access_level = Column(Text, name='access_level', nullable=True)
    description = Column(Text, name='description', nullable=True)