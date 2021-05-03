from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSagemakerNotebookInstance(Base, FormatMixins):
    __tablename__ = 'aws_sagemaker_notebook_instance'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    default_code_repository = Column('default_code_repository', Text, nullable=True)
    direct_internet_access = Column('direct_internet_access', Text, nullable=True)
    failure_reason = Column('failure_reason', Text, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    network_interface_id = Column('network_interface_id', Text, nullable=True)
    notebook_instance_lifecycle_config_name = Column('notebook_instance_lifecycle_config_name', Text, nullable=True)
    notebook_instance_status = Column('notebook_instance_status', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    root_access = Column('root_access', Text, nullable=True)
    subnet_id = Column('subnet_id', Text, nullable=True)
    url = Column('url', Text, nullable=True)
    volume_size_in_gb = Column('volume_size_in_gb', BigInteger, nullable=True)
    accelerator_types = Column('accelerator_types', JSON, nullable=True)
    additional_code_repositories = Column('additional_code_repositories', JSON, nullable=True)
    security_groups = Column('security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)