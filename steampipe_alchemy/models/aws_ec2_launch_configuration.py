from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2LaunchConfiguration(Base):
    __tablename__ = 'aws_ec2_launch_configuration'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    launch_configuration_arn = Column(name='launch_configuration_arn', type_=Text, nullable=True)
    created_time = Column(name='created_time', type_=TIMESTAMP, nullable=True)
    image_id = Column(name='image_id', type_=Text, nullable=True)
    instance_type = Column(name='instance_type', type_=Text, nullable=True)
    associate_public_ip_address = Column(name='associate_public_ip_address', type_=Boolean, nullable=True)
    kernel_id = Column(name='kernel_id', type_=Text, nullable=True)
    key_name = Column(name='key_name', type_=Text, nullable=True)
    ramdisk_id = Column(name='ramdisk_id', type_=Text, nullable=True)
    ebs_optimized = Column(name='ebs_optimized', type_=Boolean, nullable=True)
    classic_link_vpc_id = Column(name='classic_link_vpc_id', type_=Text, nullable=True)
    spot_price = Column(name='spot_price', type_=Text, nullable=True)
    user_data = Column(name='user_data', type_=Text, nullable=True)
    placement_tenancy = Column(name='placement_tenancy', type_=Text, nullable=True)
    iam_instance_profile = Column(name='iam_instance_profile', type_=Text, nullable=True)
    instance_monitoring_enabled = Column(name='instance_monitoring_enabled', type_=Boolean, nullable=True)
    metadata_options_http_endpoint = Column(name='metadata_options_http_endpoint', type_=Text, nullable=True)
    metadata_options_put_response_hop_limit = Column(name='metadata_options_put_response_hop_limit', type_=BigInteger, nullable=True)
    metadata_options_http_tokens = Column(name='metadata_options_http_tokens', type_=Text, nullable=True)
    block_device_mappings = Column(name='block_device_mappings', type_=JSON, nullable=True)
    classic_link_vpc_security_groups = Column(name='classic_link_vpc_security_groups', type_=JSON, nullable=True)
    security_groups = Column(name='security_groups', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)