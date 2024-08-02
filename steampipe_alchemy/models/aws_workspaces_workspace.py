from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWorkspacesWorkspace(Base, FormatMixins):
    __tablename__ = 'aws_workspaces_workspace'
    tags_src = Column('tags_src', JSON, nullable=True)
    root_volume_encryption_enabled = Column('root_volume_encryption_enabled', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    user_volume_encryption_enabled = Column('user_volume_encryption_enabled', Boolean, nullable=True)
    ip_address = Column('ip_address', psql.INET, nullable=True)
    modification_states = Column('modification_states', JSON, nullable=True)
    workspace_properties = Column('workspace_properties', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    workspace_id = Column('workspace_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    volume_encryption_key = Column('volume_encryption_key', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    bundle_id = Column('bundle_id', Text, nullable=True)
    directory_id = Column('directory_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    error_code = Column('error_code', Text, nullable=True)
    error_message = Column('error_message', Text, nullable=True)
    subnet_id = Column('subnet_id', Text, nullable=True)
    user_name = Column('user_name', Text, nullable=True)