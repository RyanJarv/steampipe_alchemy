from steampipe_alchemy.types.aws_rds_db_parameter_group import *

from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRdsDbParameterGroup(Base):
    __tablename__ = 'aws_rds_db_parameter_group'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    db_parameter_group_family = Column('db_parameter_group_family', Text, nullable=True)
    parameters: Parameters = Column('parameters', JSON, nullable=True)
    tags_src: TagsSrc = Column('tags_src', JSON, nullable=True)
    tags: Tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas: Akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)