from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsEc2LaunchConfiguration(Base, FormatMixins):
    __tablename__ = 'aws_ec2_launch_configuration'
    name = Column('name', Text, primary_key=True, nullable=True)
    launch_configuration_arn = Column('launch_configuration_arn', Text, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    image_id = Column('image_id', Text, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    associate_public_ip_address = Column('associate_public_ip_address', Boolean, nullable=True)
    kernel_id = Column('kernel_id', Text, nullable=True)
    key_name = Column('key_name', Text, nullable=True)
    ramdisk_id = Column('ramdisk_id', Text, nullable=True)
    ebs_optimized = Column('ebs_optimized', Boolean, nullable=True)
    classic_link_vpc_id = Column('classic_link_vpc_id', Text, nullable=True)
    spot_price = Column('spot_price', Text, nullable=True)
    user_data = Column('user_data', Text, nullable=True)
    placement_tenancy = Column('placement_tenancy', Text, nullable=True)
    iam_instance_profile = Column('iam_instance_profile', Text, nullable=True)
    instance_monitoring_enabled = Column('instance_monitoring_enabled', Boolean, nullable=True)
    metadata_options_http_endpoint = Column('metadata_options_http_endpoint', Text, nullable=True)
    metadata_options_put_response_hop_limit = Column('metadata_options_put_response_hop_limit', BigInteger, nullable=True)
    metadata_options_http_tokens = Column('metadata_options_http_tokens', Text, nullable=True)
    block_device_mappings = Column('block_device_mappings', JSON, nullable=True)
    classic_link_vpc_security_groups = Column('classic_link_vpc_security_groups', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsEc2LaunchConfigurationLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_ec2_launch_configuration_local'
    name = Column('name', Text, primary_key=True, nullable=True)
    launch_configuration_arn = Column('launch_configuration_arn', Text, nullable=True)
    created_time = Column('created_time', TIMESTAMP, nullable=True)
    image_id = Column('image_id', Text, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    associate_public_ip_address = Column('associate_public_ip_address', Boolean, nullable=True)
    kernel_id = Column('kernel_id', Text, nullable=True)
    key_name = Column('key_name', Text, nullable=True)
    ramdisk_id = Column('ramdisk_id', Text, nullable=True)
    ebs_optimized = Column('ebs_optimized', Boolean, nullable=True)
    classic_link_vpc_id = Column('classic_link_vpc_id', Text, nullable=True)
    spot_price = Column('spot_price', Text, nullable=True)
    user_data = Column('user_data', Text, nullable=True)
    placement_tenancy = Column('placement_tenancy', Text, nullable=True)
    iam_instance_profile = Column('iam_instance_profile', Text, nullable=True)
    instance_monitoring_enabled = Column('instance_monitoring_enabled', Boolean, nullable=True)
    metadata_options_http_endpoint = Column('metadata_options_http_endpoint', Text, nullable=True)
    metadata_options_put_response_hop_limit = Column('metadata_options_put_response_hop_limit', BigInteger, nullable=True)
    metadata_options_http_tokens = Column('metadata_options_http_tokens', Text, nullable=True)
    block_device_mappings = Column('block_device_mappings', JSON, nullable=True)
    classic_link_vpc_security_groups = Column('classic_link_vpc_security_groups', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsEc2LaunchConfiguration).select_from(AwsEc2LaunchConfiguration)
create_materialized_view('aws_ec2_launch_configuration_local', cache, db.metadata_materialized)
