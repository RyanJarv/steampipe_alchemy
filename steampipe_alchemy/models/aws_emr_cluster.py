from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEmrCluster(Base):
    __tablename__ = 'aws_emr_cluster'
    name = Column(Text, name='name', nullable=True)
    id = Column(Text, name='id', primary_key=True, nullable=True)
    cluster_arn = Column(Text, name='cluster_arn', nullable=True)
    status = Column(JSON, name='status', nullable=True)
    auto_scaling_role = Column(Text, name='auto_scaling_role', nullable=True)
    auto_terminate = Column(Boolean, name='auto_terminate', nullable=True)
    custom_ami_id = Column(Text, name='custom_ami_id', nullable=True)
    ebs_root_volume_size = Column(Text, name='ebs_root_volume_size', nullable=True)
    instance_collection_type = Column(Text, name='instance_collection_type', nullable=True)
    log_encryption_kms_key_id = Column(Text, name='log_encryption_kms_key_id', nullable=True)
    log_uri = Column(Text, name='log_uri', nullable=True)
    outpost_arn = Column(Text, name='outpost_arn', nullable=True)
    master_public_dns_name = Column(Text, name='master_public_dns_name', nullable=True)
    normalized_instance_hours = Column(BigInteger, name='normalized_instance_hours', nullable=True)
    release_label = Column(Text, name='release_label', nullable=True)
    repo_upgrade_on_boot = Column(Text, name='repo_upgrade_on_boot', nullable=True)
    requested_ami_version = Column(Text, name='requested_ami_version', nullable=True)
    running_ami_version = Column(Text, name='running_ami_version', nullable=True)
    scale_down_behavior = Column(Text, name='scale_down_behavior', nullable=True)
    security_configuration = Column(Text, name='security_configuration', nullable=True)
    service_role = Column(Text, name='service_role', nullable=True)
    step_concurrency_level = Column(BigInteger, name='step_concurrency_level', nullable=True)
    termination_protected = Column(Boolean, name='termination_protected', nullable=True)
    visible_to_all_users = Column(Boolean, name='visible_to_all_users', nullable=True)
    applications = Column(JSON, name='applications', nullable=True)
    configurations = Column(JSON, name='configurations', nullable=True)
    ec2_instance_attributes = Column(JSON, name='ec2_instance_attributes', nullable=True)
    placement_groups = Column(JSON, name='placement_groups', nullable=True)
    kerberos_attributes = Column(JSON, name='kerberos_attributes', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)