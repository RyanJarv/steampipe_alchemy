from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2AmiShared(Base, FormatMixins):
    __tablename__ = 'aws_ec2_ami_shared'
    tags_src = Column('tags_src', JSON, nullable=True)
    ena_support = Column('ena_support', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    public = Column('public', Boolean, nullable=True)
    block_device_mappings = Column('block_device_mappings', JSON, nullable=True)
    product_codes = Column('product_codes', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    kernel_id = Column('kernel_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    platform = Column('platform', Text, nullable=True)
    platform_details = Column('platform_details', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    root_device_name = Column('root_device_name', Text, nullable=True)
    root_device_type = Column('root_device_type', Text, nullable=True)
    sriov_net_support = Column('sriov_net_support', Text, nullable=True)
    usage_operation = Column('usage_operation', Text, nullable=True)
    virtualization_type = Column('virtualization_type', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    ramdisk_id = Column('ramdisk_id', Text, nullable=True)
    image_id = Column('image_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    image_type = Column('image_type', Text, nullable=True)
    image_location = Column('image_location', Text, nullable=True)
    architecture = Column('architecture', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    hypervisor = Column('hypervisor', Text, nullable=True)
    image_owner_alias = Column('image_owner_alias', Text, nullable=True)
    imds_support = Column('imds_support', Text, nullable=True)