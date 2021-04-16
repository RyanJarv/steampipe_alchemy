from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2LaunchConfiguration(Base):
    __tablename__ = 'aws_ec2_launch_configuration'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    launch_configuration_arn = Column(Text, name='launch_configuration_arn', nullable=True)
    created_time = Column(TIMESTAMP, name='created_time', nullable=True)
    image_id = Column(Text, name='image_id', nullable=True)
    instance_type = Column(Text, name='instance_type', nullable=True)
    associate_public_ip_address = Column(Boolean, name='associate_public_ip_address', nullable=True)
    kernel_id = Column(Text, name='kernel_id', nullable=True)
    key_name = Column(Text, name='key_name', nullable=True)
    ramdisk_id = Column(Text, name='ramdisk_id', nullable=True)
    ebs_optimized = Column(Boolean, name='ebs_optimized', nullable=True)
    classic_link_vpc_id = Column(Text, name='classic_link_vpc_id', nullable=True)
    spot_price = Column(Text, name='spot_price', nullable=True)
    user_data = Column(Text, name='user_data', nullable=True)
    placement_tenancy = Column(Text, name='placement_tenancy', nullable=True)
    iam_instance_profile = Column(Text, name='iam_instance_profile', nullable=True)
    instance_monitoring_enabled = Column(Boolean, name='instance_monitoring_enabled', nullable=True)
    metadata_options_http_endpoint = Column(Text, name='metadata_options_http_endpoint', nullable=True)
    metadata_options_put_response_hop_limit = Column(BigInteger, name='metadata_options_put_response_hop_limit', nullable=True)
    metadata_options_http_tokens = Column(Text, name='metadata_options_http_tokens', nullable=True)
    block_device_mappings = Column(JSON, name='block_device_mappings', nullable=True)
    classic_link_vpc_security_groups = Column(JSON, name='classic_link_vpc_security_groups', nullable=True)
    security_groups = Column(JSON, name='security_groups', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)