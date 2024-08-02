from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsVpcVerifiedAccessEndpoint(Base, FormatMixins):
    __tablename__ = 'aws_vpc_verified_access_endpoint'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    deletion_time = Column('deletion_time', TIMESTAMP, nullable=True)
    last_updated_time = Column('last_updated_time', TIMESTAMP, nullable=True)
    load_balancer_options = Column('load_balancer_options', JSON, nullable=True)
    network_interface_options = Column('network_interface_options', JSON, nullable=True)
    status = Column('status', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    domain_certificate_arn = Column('domain_certificate_arn', Text, nullable=True)
    endpoint_domain = Column('endpoint_domain', Text, nullable=True)
    endpoint_type = Column('endpoint_type', Text, nullable=True)
    verified_access_endpoint_id = Column('verified_access_endpoint_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    verified_access_group_id = Column('verified_access_group_id', Text, nullable=True)
    verified_access_instance_id = Column('verified_access_instance_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    status_code = Column('status_code', Text, nullable=True)
    application_domain = Column('application_domain', Text, nullable=True)
    attachment_type = Column('attachment_type', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    device_validation_domain = Column('device_validation_domain', Text, nullable=True)