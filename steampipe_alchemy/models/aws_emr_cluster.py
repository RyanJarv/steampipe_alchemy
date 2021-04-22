from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEmrCluster(Base):
    __tablename__ = 'aws_emr_cluster'
    name = Column('name', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    cluster_arn = Column('cluster_arn', Text, nullable=True)
    status = Column('status', JSON, nullable=True)
    auto_scaling_role = Column('auto_scaling_role', Text, nullable=True)
    auto_terminate = Column('auto_terminate', Boolean, nullable=True)
    custom_ami_id = Column('custom_ami_id', Text, nullable=True)
    ebs_root_volume_size = Column('ebs_root_volume_size', Text, nullable=True)
    instance_collection_type = Column('instance_collection_type', Text, nullable=True)
    log_encryption_kms_key_id = Column('log_encryption_kms_key_id', Text, nullable=True)
    log_uri = Column('log_uri', Text, nullable=True)
    outpost_arn = Column('outpost_arn', Text, nullable=True)
    master_public_dns_name = Column('master_public_dns_name', Text, nullable=True)
    normalized_instance_hours = Column('normalized_instance_hours', BigInteger, nullable=True)
    release_label = Column('release_label', Text, nullable=True)
    repo_upgrade_on_boot = Column('repo_upgrade_on_boot', Text, nullable=True)
    requested_ami_version = Column('requested_ami_version', Text, nullable=True)
    running_ami_version = Column('running_ami_version', Text, nullable=True)
    scale_down_behavior = Column('scale_down_behavior', Text, nullable=True)
    security_configuration = Column('security_configuration', Text, nullable=True)
    service_role = Column('service_role', Text, nullable=True)
    step_concurrency_level = Column('step_concurrency_level', BigInteger, nullable=True)
    termination_protected = Column('termination_protected', Boolean, nullable=True)
    visible_to_all_users = Column('visible_to_all_users', Boolean, nullable=True)
    applications = Column('applications', JSON, nullable=True)
    configurations = Column('configurations', JSON, nullable=True)
    ec2_instance_attributes = Column('ec2_instance_attributes', JSON, nullable=True)
    placement_groups = Column('placement_groups', JSON, nullable=True)
    kerberos_attributes = Column('kerberos_attributes', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)