from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2Ami(Base):
    __tablename__ = 'aws_ec2_ami'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    image_id = Column(Text, name='image_id', nullable=True)
    state = Column(Text, name='state', nullable=True)
    image_type = Column(Text, name='image_type', nullable=True)
    image_location = Column(Text, name='image_location', nullable=True)
    creation_date = Column(TIMESTAMP, name='creation_date', nullable=True)
    architecture = Column(Text, name='architecture', nullable=True)
    description = Column(Text, name='description', nullable=True)
    ena_support = Column(Boolean, name='ena_support', nullable=True)
    hypervisor = Column(Text, name='hypervisor', nullable=True)
    image_owner_alias = Column(Text, name='image_owner_alias', nullable=True)
    kernel_id = Column(Text, name='kernel_id', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    platform = Column(Text, name='platform', nullable=True)
    platform_details = Column(Text, name='platform_details', nullable=True)
    public = Column(Boolean, name='public', nullable=True)
    ramdisk_id = Column(Text, name='ramdisk_id', nullable=True)
    root_device_name = Column(Text, name='root_device_name', nullable=True)
    root_device_type = Column(Text, name='root_device_type', nullable=True)
    sriov_net_support = Column(Text, name='sriov_net_support', nullable=True)
    usage_operation = Column(Text, name='usage_operation', nullable=True)
    virtualization_type = Column(Text, name='virtualization_type', nullable=True)
    block_device_mappings = Column(JSON, name='block_device_mappings', nullable=True)
    product_codes = Column(JSON, name='product_codes', nullable=True)
    launch_permissions = Column(JSON, name='launch_permissions', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)