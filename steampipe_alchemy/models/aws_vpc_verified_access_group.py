from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcVerifiedAccessGroup(Base, FormatMixins):
    __tablename__ = 'aws_vpc_verified_access_group'
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    last_updated_time = Column('last_updated_time', TIMESTAMP, nullable=True)
    deletion_time = Column('deletion_time', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    verified_access_instance_id = Column('verified_access_instance_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    verified_access_group_id = Column('verified_access_group_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)