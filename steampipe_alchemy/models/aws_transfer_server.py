from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsTransferServer(Base, FormatMixins):
    __tablename__ = 'aws_transfer_server'
    _ctx = Column('_ctx', JSON, nullable=True)
    user_count = Column('user_count', BigInteger, nullable=True)
    identity_provider_details = Column('identity_provider_details', JSON, nullable=True)
    protocol_details = Column('protocol_details', JSON, nullable=True)
    endpoint_details = Column('endpoint_details', JSON, nullable=True)
    protocols = Column('protocols', JSON, nullable=True)
    workflow_details = Column('workflow_details', JSON, nullable=True)
    structured_log_destinations = Column('structured_log_destinations', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    post_authentication_login_banner = Column('post_authentication_login_banner', Text, nullable=True)
    security_policy_name = Column('security_policy_name', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    server_id = Column('server_id', Text, nullable=True)
    domain = Column('domain', Text, nullable=True)
    identity_provider_type = Column('identity_provider_type', Text, nullable=True)
    endpoint_type = Column('endpoint_type', Text, nullable=True)
    logging_role = Column('logging_role', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    certificate = Column('certificate', Text, nullable=True)
    host_key_fingerprint = Column('host_key_fingerprint', Text, nullable=True)
    pre_authentication_login_banner = Column('pre_authentication_login_banner', Text, nullable=True)