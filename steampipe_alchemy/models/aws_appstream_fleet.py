from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAppstreamFleet(Base, FormatMixins):
    __tablename__ = 'aws_appstream_fleet'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    disconnect_timeout_in_seconds = Column('disconnect_timeout_in_seconds', BigInteger, nullable=True)
    enable_default_internet_access = Column('enable_default_internet_access', Boolean, nullable=True)
    idle_disconnect_timeout_in_seconds = Column('idle_disconnect_timeout_in_seconds', BigInteger, nullable=True)
    max_concurrent_sessions = Column('max_concurrent_sessions', BigInteger, nullable=True)
    max_user_duration_in_seconds = Column('max_user_duration_in_seconds', BigInteger, nullable=True)
    compute_capacity_status = Column('compute_capacity_status', JSON, nullable=True)
    fleet_errors = Column('fleet_errors', JSON, nullable=True)
    session_script_s3_location = Column('session_script_s3_location', JSON, nullable=True)
    usb_device_filter_strings = Column('usb_device_filter_strings', JSON, nullable=True)
    vpc_config = Column('vpc_config', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    image_name = Column('image_name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    platform = Column('platform', Text, nullable=True)
    stream_view = Column('stream_view', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    display_name = Column('display_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    directory_name = Column('directory_name', Text, nullable=True)
    organizational_unit_distinguished_name = Column('organizational_unit_distinguished_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    fleet_type = Column('fleet_type', Text, nullable=True)
    iam_role_arn = Column('iam_role_arn', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    image_arn = Column('image_arn', Text, nullable=True)