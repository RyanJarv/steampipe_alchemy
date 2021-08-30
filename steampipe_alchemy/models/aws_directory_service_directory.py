from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDirectoryServiceDirectory(Base, FormatMixins):
    __tablename__ = 'aws_directory_service_directory'
    connect_settings = Column('connect_settings', JSON, nullable=True)
    dns_ip_addrs = Column('dns_ip_addrs', JSON, nullable=True)
    owner_directory_description = Column('owner_directory_description', JSON, nullable=True)
    radius_settings = Column('radius_settings', JSON, nullable=True)
    regions_info = Column('regions_info', JSON, nullable=True)
    vpc_settings = Column('vpc_settings', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    launch_time = Column('launch_time', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sso_enabled = Column('sso_enabled', Boolean, nullable=True)
    stage_last_updated_date_time = Column('stage_last_updated_date_time', TIMESTAMP, nullable=True)
    desired_number_of_domain_controllers = Column('desired_number_of_domain_controllers', BigInteger, nullable=True)
    short_name = Column('short_name', Text, nullable=True)
    size = Column('size', Text, nullable=True)
    stage_reason = Column('stage_reason', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    directory_id = Column('directory_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    stage = Column('stage', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    access_url = Column('access_url', Text, nullable=True)
    alias = Column('alias', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    edition = Column('edition', Text, nullable=True)
    radius_status = Column('radius_status', Text, nullable=True)
    share_method = Column('share_method', Text, nullable=True)
    share_notes = Column('share_notes', Text, nullable=True)
    share_status = Column('share_status', Text, nullable=True)