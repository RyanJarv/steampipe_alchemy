from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2InstanceType(Base):
    __tablename__ = 'aws_ec2_instance_type'
    instance_type = Column(name='instance_type', type_=Text, nullable=True)
    auto_recovery_supported = Column(name='auto_recovery_supported', type_=Boolean, nullable=True)
    bare_metal = Column(name='bare_metal', type_=Boolean, nullable=True)
    burstable_performance_supported = Column(name='burstable_performance_supported', type_=Boolean, nullable=True)
    current_generation = Column(name='current_generation', type_=Boolean, nullable=True)
    dedicated_hosts_supported = Column(name='dedicated_hosts_supported', type_=Boolean, nullable=True)
    free_tier_eligible = Column(name='free_tier_eligible', type_=Boolean, nullable=True)
    hibernation_supported = Column(name='hibernation_supported', type_=Boolean, nullable=True)
    hypervisor = Column(name='hypervisor', type_=Text, nullable=True)
    instance_storage_supported = Column(name='instance_storage_supported', type_=Text, nullable=True)
    ebs_info = Column(name='ebs_info', type_=JSON, nullable=True)
    memory_info = Column(name='memory_info', type_=JSON, nullable=True)
    network_info = Column(name='network_info', type_=JSON, nullable=True)
    placement_group_info = Column(name='placement_group_info', type_=JSON, nullable=True)
    processor_info = Column(name='processor_info', type_=JSON, nullable=True)
    supported_root_device_types = Column(name='supported_root_device_types', type_=JSON, nullable=True)
    supported_usage_classes = Column(name='supported_usage_classes', type_=JSON, nullable=True)
    supported_virtualization_types = Column(name='supported_virtualization_types', type_=JSON, nullable=True)
    v_cpu_info = Column(name='v_cpu_info', type_=JSON, nullable=True)
    gpu_info = Column(name='gpu_info', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)