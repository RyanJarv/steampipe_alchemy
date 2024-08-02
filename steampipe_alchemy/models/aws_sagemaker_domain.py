from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSagemakerDomain(Base, FormatMixins):
    __tablename__ = 'aws_sagemaker_domain'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    default_user_settings = Column('default_user_settings', JSON, nullable=True)
    domain_settings = Column('domain_settings', JSON, nullable=True)
    subnet_ids = Column('subnet_ids', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    security_group_id_for_domain_boundary = Column('security_group_id_for_domain_boundary', Text, nullable=True)
    single_sign_on_managed_application_instance_id = Column('single_sign_on_managed_application_instance_id', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    url = Column('url', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    app_network_access_type = Column('app_network_access_type', Text, nullable=True)
    app_security_group_management = Column('app_security_group_management', Text, nullable=True)
    auth_mode = Column('auth_mode', Text, nullable=True)
    failure_reason = Column('failure_reason', Text, nullable=True)
    home_efs_file_system_id = Column('home_efs_file_system_id', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)