from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsIamAction(Base, FormatMixins):
    __tablename__ = 'aws_iam_action'
    action = Column('action', Text, primary_key=True, nullable=True)
    prefix = Column('prefix', Text, nullable=True)
    privilege = Column('privilege', Text, nullable=True)
    access_level = Column('access_level', Text, nullable=True)
    description = Column('description', Text, nullable=True)


# Local materialized view table
class AwsIamActionLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_iam_action_local'
    action = Column('action', Text, primary_key=True, nullable=True)
    prefix = Column('prefix', Text, nullable=True)
    privilege = Column('privilege', Text, nullable=True)
    access_level = Column('access_level', Text, nullable=True)
    description = Column('description', Text, nullable=True)


cache = select(AwsIamAction).select_from(AwsIamAction)
create_materialized_view('aws_iam_action_local', cache, db.metadata_materialized)
