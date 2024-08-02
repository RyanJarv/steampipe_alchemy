from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2LaunchTemplateVersion(Base, FormatMixins):
    __tablename__ = 'aws_ec2_launch_template_version'
    disable_api_termination = Column('disable_api_termination', Boolean, nullable=True)
    launch_template_data = Column('launch_template_data', JSON, nullable=True)
    ebs_optimized = Column('ebs_optimized', Boolean, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    default_version = Column('default_version', Boolean, nullable=True)
    disable_api_stop = Column('disable_api_stop', Boolean, nullable=True)
    version_number = Column('version_number', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    security_group_ids = Column('security_group_ids', Text, nullable=True)
    version_description = Column('version_description', Text, nullable=True)
    user_data = Column('user_data', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    security_groups = Column('security_groups', Text, nullable=True)
    launch_template_id = Column('launch_template_id', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    image_id = Column('image_id', Text, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    kernel_id = Column('kernel_id', Text, nullable=True)
    key_name = Column('key_name', Text, nullable=True)
    ram_disk_id = Column('ram_disk_id', Text, nullable=True)
    launch_template_name = Column('launch_template_name', Text, nullable=True)