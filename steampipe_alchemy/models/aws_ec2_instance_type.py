from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2InstanceType(Base, FormatMixins):
    __tablename__ = 'aws_ec2_instance_type'
    _ctx = Column('_ctx', JSON, nullable=True)
    auto_recovery_supported = Column('auto_recovery_supported', Boolean, nullable=True)
    bare_metal = Column('bare_metal', Boolean, nullable=True)
    burstable_performance_supported = Column('burstable_performance_supported', Boolean, nullable=True)
    current_generation = Column('current_generation', Boolean, nullable=True)
    dedicated_hosts_supported = Column('dedicated_hosts_supported', Boolean, nullable=True)
    free_tier_eligible = Column('free_tier_eligible', Boolean, nullable=True)
    hibernation_supported = Column('hibernation_supported', Boolean, nullable=True)
    processor_info = Column('processor_info', JSON, nullable=True)
    supported_root_device_types = Column('supported_root_device_types', JSON, nullable=True)
    supported_usage_classes = Column('supported_usage_classes', JSON, nullable=True)
    supported_virtualization_types = Column('supported_virtualization_types', JSON, nullable=True)
    v_cpu_info = Column('v_cpu_info', JSON, nullable=True)
    gpu_info = Column('gpu_info', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    ebs_info = Column('ebs_info', JSON, nullable=True)
    memory_info = Column('memory_info', JSON, nullable=True)
    network_info = Column('network_info', JSON, nullable=True)
    placement_group_info = Column('placement_group_info', JSON, nullable=True)
    hypervisor = Column('hypervisor', Text, nullable=True)
    instance_storage_supported = Column('instance_storage_supported', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)