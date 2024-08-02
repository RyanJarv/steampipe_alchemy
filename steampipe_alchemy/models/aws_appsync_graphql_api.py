from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAppsyncGraphqlApi(Base, FormatMixins):
    __tablename__ = 'aws_appsync_graphql_api'
    _ctx = Column('_ctx', JSON, nullable=True)
    xray_enabled = Column('xray_enabled', Boolean, nullable=True)
    log_config = Column('log_config', JSON, nullable=True)
    open_id_connect_config = Column('open_id_connect_config', JSON, nullable=True)
    additional_authentication_providers = Column('additional_authentication_providers', JSON, nullable=True)
    dns = Column('dns', JSON, nullable=True)
    lambda_authorizer_config = Column('lambda_authorizer_config', JSON, nullable=True)
    uris = Column('uris', JSON, nullable=True)
    user_pool_config = Column('user_pool_config', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    api_id = Column('api_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    api_type = Column('api_type', Text, nullable=True)
    authentication_type = Column('authentication_type', Text, nullable=True)
    merged_api_execution_role_arn = Column('merged_api_execution_role_arn', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    owner_contact = Column('owner_contact', Text, nullable=True)
    visibility = Column('visibility', Text, nullable=True)
    waf_web_acl_arn = Column('waf_web_acl_arn', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)