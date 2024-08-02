from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAppstreamImage(Base, FormatMixins):
    __tablename__ = 'aws_appstream_image'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    image_builder_supported = Column('image_builder_supported', Boolean, nullable=True)
    public_base_image_released_date = Column('public_base_image_released_date', TIMESTAMP, nullable=True)
    applications = Column('applications', JSON, nullable=True)
    image_errors = Column('image_errors', JSON, nullable=True)
    image_permissions = Column('image_permissions', JSON, nullable=True)
    state_change_reason = Column('state_change_reason', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    state = Column('state', Text, nullable=True)
    visibility = Column('visibility', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    appstream_agent_version = Column('appstream_agent_version', Text, nullable=True)
    base_image_arn = Column('base_image_arn', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    display_name = Column('display_name', Text, nullable=True)
    image_builder_name = Column('image_builder_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    platform = Column('platform', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)