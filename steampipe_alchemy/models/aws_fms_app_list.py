from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsFmsAppList(Base, FormatMixins):
    __tablename__ = 'aws_fms_app_list'
    akas = Column('akas', JSON, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    previous_apps_list = Column('previous_apps_list', JSON, nullable=True)
    apps_list = Column('apps_list', JSON, nullable=True)
    last_update_time = Column('last_update_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    list_id = Column('list_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    list_update_token = Column('list_update_token', Text, nullable=True)
    list_name = Column('list_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)