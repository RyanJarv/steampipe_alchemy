from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsIamAction(Base, FormatMixins):
    __tablename__ = 'aws_iam_action'
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    privilege = Column('privilege', Text, nullable=True)
    access_level = Column('access_level', Text, nullable=True)
    action = Column('action', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    prefix = Column('prefix', Text, nullable=True)