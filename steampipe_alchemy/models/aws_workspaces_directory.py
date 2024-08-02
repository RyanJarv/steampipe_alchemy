from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWorkspacesDirectory(Base, FormatMixins):
    __tablename__ = 'aws_workspaces_directory'
    _ctx = Column('_ctx', JSON, nullable=True)
    certificate_based_auth_properties = Column('certificate_based_auth_properties', JSON, nullable=True)
    dns_ip_addresses = Column('dns_ip_addresses', JSON, nullable=True)
    saml_properties = Column('saml_properties', JSON, nullable=True)
    selfservice_permissions = Column('selfservice_permissions', JSON, nullable=True)
    subnet_ids = Column('subnet_ids', JSON, nullable=True)
    workspace_access_properties = Column('workspace_access_properties', JSON, nullable=True)
    workspace_creation_properties = Column('workspace_creation_properties', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    directory_id = Column('directory_id', Text, nullable=True)
    tenancy = Column('tenancy', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    alias = Column('alias', Text, nullable=True)
    workspace_security_group_id = Column('workspace_security_group_id', Text, nullable=True)
    customer_user_name = Column('customer_user_name', Text, nullable=True)
    directory_type = Column('directory_type', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    iam_role_id = Column('iam_role_id', Text, nullable=True)
    ip_group_ids = Column('ip_group_ids', Text, nullable=True)
    registration_code = Column('registration_code', Text, nullable=True)
    title = Column('title', Text, nullable=True)