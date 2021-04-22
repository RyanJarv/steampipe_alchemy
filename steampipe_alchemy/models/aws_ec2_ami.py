from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2Ami(Base):
    __tablename__ = 'aws_ec2_ami'
    name = Column('name', Text, primary_key=True, nullable=True)
    image_id = Column('image_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    image_type = Column('image_type', Text, nullable=True)
    image_location = Column('image_location', Text, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    architecture = Column('architecture', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    ena_support = Column('ena_support', Boolean, nullable=True)
    hypervisor = Column('hypervisor', Text, nullable=True)
    image_owner_alias = Column('image_owner_alias', Text, nullable=True)
    kernel_id = Column('kernel_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    platform = Column('platform', Text, nullable=True)
    platform_details = Column('platform_details', Text, nullable=True)
    public = Column('public', Boolean, nullable=True)
    ramdisk_id = Column('ramdisk_id', Text, nullable=True)
    root_device_name = Column('root_device_name', Text, nullable=True)
    root_device_type = Column('root_device_type', Text, nullable=True)
    sriov_net_support = Column('sriov_net_support', Text, nullable=True)
    usage_operation = Column('usage_operation', Text, nullable=True)
    virtualization_type = Column('virtualization_type', Text, nullable=True)
    block_device_mappings = Column('block_device_mappings', JSON, nullable=True)
    product_codes = Column('product_codes', JSON, nullable=True)
    launch_permissions = Column('launch_permissions', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)