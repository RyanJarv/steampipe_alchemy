from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2Ami(Base):
    __tablename__ = 'aws_ec2_ami'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    image_id = Column(name='image_id', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    image_type = Column(name='image_type', type_=Text, nullable=True)
    image_location = Column(name='image_location', type_=Text, nullable=True)
    creation_date = Column(name='creation_date', type_=TIMESTAMP, nullable=True)
    architecture = Column(name='architecture', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    ena_support = Column(name='ena_support', type_=Boolean, nullable=True)
    hypervisor = Column(name='hypervisor', type_=Text, nullable=True)
    image_owner_alias = Column(name='image_owner_alias', type_=Text, nullable=True)
    kernel_id = Column(name='kernel_id', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    platform = Column(name='platform', type_=Text, nullable=True)
    platform_details = Column(name='platform_details', type_=Text, nullable=True)
    public = Column(name='public', type_=Boolean, nullable=True)
    ramdisk_id = Column(name='ramdisk_id', type_=Text, nullable=True)
    root_device_name = Column(name='root_device_name', type_=Text, nullable=True)
    root_device_type = Column(name='root_device_type', type_=Text, nullable=True)
    sriov_net_support = Column(name='sriov_net_support', type_=Text, nullable=True)
    usage_operation = Column(name='usage_operation', type_=Text, nullable=True)
    virtualization_type = Column(name='virtualization_type', type_=Text, nullable=True)
    block_device_mappings = Column(name='block_device_mappings', type_=JSON, nullable=True)
    product_codes = Column(name='product_codes', type_=JSON, nullable=True)
    launch_permissions = Column(name='launch_permissions', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)