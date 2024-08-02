from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRdsDbOptionGroup(Base, FormatMixins):
    __tablename__ = 'aws_rds_db_option_group'
    _ctx = Column('_ctx', JSON, nullable=True)
    allows_vpc_and_non_vpc_instance_memberships = Column('allows_vpc_and_non_vpc_instance_memberships', Boolean, nullable=True)
    options = Column('options', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    engine_name = Column('engine_name', Text, nullable=True)
    major_engine_version = Column('major_engine_version', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)