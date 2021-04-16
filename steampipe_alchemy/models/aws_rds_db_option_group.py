from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRdsDbOptionGroup(Base):
    __tablename__ = 'aws_rds_db_option_group'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    description = Column(Text, name='description', nullable=True)
    allows_vpc_and_non_vpc_instance_memberships = Column(Boolean, name='allows_vpc_and_non_vpc_instance_memberships', nullable=True)
    engine_name = Column(Text, name='engine_name', nullable=True)
    major_engine_version = Column(Text, name='major_engine_version', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    options = Column(JSON, name='options', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)