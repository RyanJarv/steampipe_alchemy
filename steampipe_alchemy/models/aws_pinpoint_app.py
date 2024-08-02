from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsPinpointApp(Base, FormatMixins):
    __tablename__ = 'aws_pinpoint_app'
    last_modified_date = Column('last_modified_date', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    campaign_hook = Column('campaign_hook', JSON, nullable=True)
    limits = Column('limits', JSON, nullable=True)
    quiet_time = Column('quiet_time', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    id = Column('id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)