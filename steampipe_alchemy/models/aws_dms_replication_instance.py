from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDmsReplicationInstance(Base, FormatMixins):
    __tablename__ = 'aws_dms_replication_instance'
    auto_minor_version_upgrade = Column('auto_minor_version_upgrade', Boolean, nullable=True)
    pending_modified_values = Column('pending_modified_values', JSON, nullable=True)
    replication_instance_private_ip_addresses = Column('replication_instance_private_ip_addresses', JSON, nullable=True)
    replication_instance_public_ip_addresses = Column('replication_instance_public_ip_addresses', JSON, nullable=True)
    replication_subnet_group = Column('replication_subnet_group', JSON, nullable=True)
    vpc_security_groups = Column('vpc_security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    multi_az = Column('multi_az', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    publicly_accessible = Column('publicly_accessible', Boolean, nullable=True)
    allocated_storage = Column('allocated_storage', BigInteger, nullable=True)
    free_until = Column('free_until', TIMESTAMP, nullable=True)
    instance_create_time = Column('instance_create_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    replication_instance_status = Column('replication_instance_status', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    replication_instance_class = Column('replication_instance_class', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    dns_name_servers = Column('dns_name_servers', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    replication_instance_private_ip_address = Column('replication_instance_private_ip_address', Text, nullable=True)
    replication_instance_public_ip_address = Column('replication_instance_public_ip_address', Text, nullable=True)
    replication_instance_identifier = Column('replication_instance_identifier', Text, nullable=True)
    secondary_availability_zone = Column('secondary_availability_zone', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)