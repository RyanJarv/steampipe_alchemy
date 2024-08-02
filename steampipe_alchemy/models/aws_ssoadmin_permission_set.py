from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsoadminPermissionSet(Base, FormatMixins):
    __tablename__ = 'aws_ssoadmin_permission_set'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    session_duration = Column('session_duration', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    region = Column('region', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    instance_arn = Column('instance_arn', Text, nullable=True)
    relay_state = Column('relay_state', Text, nullable=True)