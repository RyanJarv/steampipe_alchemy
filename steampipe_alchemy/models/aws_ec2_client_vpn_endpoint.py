from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2ClientVpnEndpoint(Base, FormatMixins):
    __tablename__ = 'aws_ec2_client_vpn_endpoint'
    _ctx = Column('_ctx', JSON, nullable=True)
    vpn_port = Column('vpn_port', BigInteger, nullable=True)
    authentication_options = Column('authentication_options', JSON, nullable=True)
    client_connect_options = Column('client_connect_options', JSON, nullable=True)
    connection_log_options = Column('connection_log_options', JSON, nullable=True)
    client_login_banner_options = Column('client_login_banner_options', JSON, nullable=True)
    dns_servers = Column('dns_servers', JSON, nullable=True)
    security_group_ids = Column('security_group_ids', JSON, nullable=True)
    status = Column('status', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    vpn_protocol = Column('vpn_protocol', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    client_cidr_block = Column('client_cidr_block', psql.CIDR, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    deletion_time = Column('deletion_time', TIMESTAMP, nullable=True)
    session_timeout_hours = Column('session_timeout_hours', BigInteger, nullable=True)
    split_tunnel = Column('split_tunnel', Boolean, nullable=True)
    transport_protocol = Column('transport_protocol', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    dns_name = Column('dns_name', Text, nullable=True)
    self_service_portal_url = Column('self_service_portal_url', Text, nullable=True)
    server_certificate_arn = Column('server_certificate_arn', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    client_vpn_endpoint_id = Column('client_vpn_endpoint_id', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)