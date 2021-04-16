from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2InstanceType(Base):
    __tablename__ = 'aws_ec2_instance_type'
    instance_type = Column(Text, name='instance_type', nullable=True)
    auto_recovery_supported = Column(Boolean, name='auto_recovery_supported', nullable=True)
    bare_metal = Column(Boolean, name='bare_metal', nullable=True)
    burstable_performance_supported = Column(Boolean, name='burstable_performance_supported', nullable=True)
    current_generation = Column(Boolean, name='current_generation', nullable=True)
    dedicated_hosts_supported = Column(Boolean, name='dedicated_hosts_supported', nullable=True)
    free_tier_eligible = Column(Boolean, name='free_tier_eligible', nullable=True)
    hibernation_supported = Column(Boolean, name='hibernation_supported', nullable=True)
    hypervisor = Column(Text, name='hypervisor', nullable=True)
    instance_storage_supported = Column(Text, name='instance_storage_supported', nullable=True)
    ebs_info = Column(JSON, name='ebs_info', nullable=True)
    memory_info = Column(JSON, name='memory_info', nullable=True)
    network_info = Column(JSON, name='network_info', nullable=True)
    placement_group_info = Column(JSON, name='placement_group_info', nullable=True)
    processor_info = Column(JSON, name='processor_info', nullable=True)
    supported_root_device_types = Column(JSON, name='supported_root_device_types', nullable=True)
    supported_usage_classes = Column(JSON, name='supported_usage_classes', nullable=True)
    supported_virtualization_types = Column(JSON, name='supported_virtualization_types', nullable=True)
    v_cpu_info = Column(JSON, name='v_cpu_info', nullable=True)
    gpu_info = Column(JSON, name='gpu_info', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)