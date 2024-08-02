from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAmplifyApp(Base, FormatMixins):
    __tablename__ = 'aws_amplify_app'
    enable_basic_auth = Column('enable_basic_auth', Boolean, nullable=True)
    auto_branch_creation_config = Column('auto_branch_creation_config', JSON, nullable=True)
    auto_branch_creation_patterns = Column('auto_branch_creation_patterns', JSON, nullable=True)
    build_spec = Column('build_spec', JSON, nullable=True)
    custom_rules = Column('custom_rules', JSON, nullable=True)
    environment_variables = Column('environment_variables', JSON, nullable=True)
    production_branch = Column('production_branch', JSON, nullable=True)
    enable_branch_auto_build = Column('enable_branch_auto_build', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    enable_branch_auto_deletion = Column('enable_branch_auto_deletion', Boolean, nullable=True)
    update_time = Column('update_time', TIMESTAMP, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    enable_auto_branch_creation = Column('enable_auto_branch_creation', Boolean, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    repository_clone_method = Column('repository_clone_method', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    name = Column('name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    basic_auth_credentials = Column('basic_auth_credentials', Text, nullable=True)
    custom_headers = Column('custom_headers', Text, nullable=True)
    default_domain = Column('default_domain', Text, nullable=True)
    iam_service_role_arn = Column('iam_service_role_arn', Text, nullable=True)
    platform = Column('platform', Text, nullable=True)
    repository = Column('repository', Text, nullable=True)
    app_id = Column('app_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)