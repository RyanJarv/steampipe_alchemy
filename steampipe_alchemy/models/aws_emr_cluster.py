from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEmrCluster(Base):
    __tablename__ = 'aws_emr_cluster'
    name = Column(name='name', type_=Text, nullable=True)
    id = Column(name='id', type_=Text, primary_key=True, nullable=True)
    cluster_arn = Column(name='cluster_arn', type_=Text, nullable=True)
    status = Column(name='status', type_=JSON, nullable=True)
    auto_scaling_role = Column(name='auto_scaling_role', type_=Text, nullable=True)
    auto_terminate = Column(name='auto_terminate', type_=Boolean, nullable=True)
    custom_ami_id = Column(name='custom_ami_id', type_=Text, nullable=True)
    ebs_root_volume_size = Column(name='ebs_root_volume_size', type_=Text, nullable=True)
    instance_collection_type = Column(name='instance_collection_type', type_=Text, nullable=True)
    log_encryption_kms_key_id = Column(name='log_encryption_kms_key_id', type_=Text, nullable=True)
    log_uri = Column(name='log_uri', type_=Text, nullable=True)
    outpost_arn = Column(name='outpost_arn', type_=Text, nullable=True)
    master_public_dns_name = Column(name='master_public_dns_name', type_=Text, nullable=True)
    normalized_instance_hours = Column(name='normalized_instance_hours', type_=BigInteger, nullable=True)
    release_label = Column(name='release_label', type_=Text, nullable=True)
    repo_upgrade_on_boot = Column(name='repo_upgrade_on_boot', type_=Text, nullable=True)
    requested_ami_version = Column(name='requested_ami_version', type_=Text, nullable=True)
    running_ami_version = Column(name='running_ami_version', type_=Text, nullable=True)
    scale_down_behavior = Column(name='scale_down_behavior', type_=Text, nullable=True)
    security_configuration = Column(name='security_configuration', type_=Text, nullable=True)
    service_role = Column(name='service_role', type_=Text, nullable=True)
    step_concurrency_level = Column(name='step_concurrency_level', type_=BigInteger, nullable=True)
    termination_protected = Column(name='termination_protected', type_=Boolean, nullable=True)
    visible_to_all_users = Column(name='visible_to_all_users', type_=Boolean, nullable=True)
    applications = Column(name='applications', type_=JSON, nullable=True)
    configurations = Column(name='configurations', type_=JSON, nullable=True)
    ec2_instance_attributes = Column(name='ec2_instance_attributes', type_=JSON, nullable=True)
    placement_groups = Column(name='placement_groups', type_=JSON, nullable=True)
    kerberos_attributes = Column(name='kerberos_attributes', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)