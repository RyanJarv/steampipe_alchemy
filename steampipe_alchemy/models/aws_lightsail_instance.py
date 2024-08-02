from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsLightsailInstance(Base, FormatMixins):
    __tablename__ = 'aws_lightsail_instance'
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    metadata_options = Column('metadata_options', JSON, nullable=True)
    networking = Column('networking', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    hardware = Column('hardware', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    ip_address_type = Column('ip_address_type', JSON, nullable=True)
    ip_v6_addresses = Column('ip_v6_addresses', JSON, nullable=True)
    is_static_ip = Column('is_static_ip', Boolean, nullable=True)
    state_code = Column('state_code', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    blueprint_id = Column('blueprint_id', Text, nullable=True)
    blueprint_name = Column('blueprint_name', Text, nullable=True)
    bundle_id = Column('bundle_id', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    private_ip_address = Column('private_ip_address', Text, nullable=True)
    public_ip_address = Column('public_ip_address', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    ssh_key_name = Column('ssh_key_name', Text, nullable=True)
    state_name = Column('state_name', Text, nullable=True)
    support_code = Column('support_code', Text, nullable=True)
    username = Column('username', Text, nullable=True)