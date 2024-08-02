from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudtrailChannel(Base, FormatMixins):
    __tablename__ = 'aws_cloudtrail_channel'
    _ctx = Column('_ctx', JSON, nullable=True)
    apply_to_all_regions = Column('apply_to_all_regions', Boolean, nullable=True)
    advanced_event_selectors = Column('advanced_event_selectors', JSON, nullable=True)
    destinations = Column('destinations', JSON, nullable=True)
    source_config = Column('source_config', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    name = Column('name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    source = Column('source', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)