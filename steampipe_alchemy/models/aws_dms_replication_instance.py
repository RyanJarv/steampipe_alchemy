from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsDmsReplicationInstance(Base, FormatMixins):
    __tablename__ = 'aws_dms_replication_instance'
    replication_instance_identifier = Column('replication_instance_identifier', Text, nullable=True)
    replication_instance_arn = Column('replication_instance_arn', Text, nullable=True)
    replication_instance_class = Column('replication_instance_class', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    publicly_accessible = Column('publicly_accessible', Boolean, nullable=True)
    allocated_storage = Column('allocated_storage', BigInteger, nullable=True)
    auto_minor_version_upgrade = Column('auto_minor_version_upgrade', Boolean, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    dns_name_servers = Column('dns_name_servers', Text, nullable=True)
    free_until = Column('free_until', TIMESTAMP, nullable=True)
    instance_create_time = Column('instance_create_time', TIMESTAMP, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    multi_az = Column('multi_az', Boolean, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    replication_instance_private_ip_address = Column('replication_instance_private_ip_address', Text, nullable=True)
    replication_instance_public_ip_address = Column('replication_instance_public_ip_address', Text, nullable=True)
    replication_instance_status = Column('replication_instance_status', Text, nullable=True)
    secondary_availability_zone = Column('secondary_availability_zone', Text, nullable=True)
    pending_modified_values = Column('pending_modified_values', JSON, nullable=True)
    replication_instance_private_ip_addresses = Column('replication_instance_private_ip_addresses', JSON, nullable=True)
    replication_instance_public_ip_addresses = Column('replication_instance_public_ip_addresses', JSON, nullable=True)
    replication_subnet_group = Column('replication_subnet_group', JSON, nullable=True)
    vpc_security_groups = Column('vpc_security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsDmsReplicationInstanceLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_dms_replication_instance_local'
    replication_instance_identifier = Column('replication_instance_identifier', Text, nullable=True)
    replication_instance_arn = Column('replication_instance_arn', Text, nullable=True)
    replication_instance_class = Column('replication_instance_class', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    publicly_accessible = Column('publicly_accessible', Boolean, nullable=True)
    allocated_storage = Column('allocated_storage', BigInteger, nullable=True)
    auto_minor_version_upgrade = Column('auto_minor_version_upgrade', Boolean, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    dns_name_servers = Column('dns_name_servers', Text, nullable=True)
    free_until = Column('free_until', TIMESTAMP, nullable=True)
    instance_create_time = Column('instance_create_time', TIMESTAMP, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    multi_az = Column('multi_az', Boolean, nullable=True)
    preferred_maintenance_window = Column('preferred_maintenance_window', Text, nullable=True)
    replication_instance_private_ip_address = Column('replication_instance_private_ip_address', Text, nullable=True)
    replication_instance_public_ip_address = Column('replication_instance_public_ip_address', Text, nullable=True)
    replication_instance_status = Column('replication_instance_status', Text, nullable=True)
    secondary_availability_zone = Column('secondary_availability_zone', Text, nullable=True)
    pending_modified_values = Column('pending_modified_values', JSON, nullable=True)
    replication_instance_private_ip_addresses = Column('replication_instance_private_ip_addresses', JSON, nullable=True)
    replication_instance_public_ip_addresses = Column('replication_instance_public_ip_addresses', JSON, nullable=True)
    replication_subnet_group = Column('replication_subnet_group', JSON, nullable=True)
    vpc_security_groups = Column('vpc_security_groups', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsDmsReplicationInstance).select_from(AwsDmsReplicationInstance)
create_materialized_view('aws_dms_replication_instance_local', cache, db.metadata_materialized)
