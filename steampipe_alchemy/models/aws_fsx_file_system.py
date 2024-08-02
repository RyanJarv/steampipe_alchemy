from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsFsxFileSystem(Base, FormatMixins):
    __tablename__ = 'aws_fsx_file_system'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    storage_capacity = Column('storage_capacity', BigInteger, nullable=True)
    administrative_actions = Column('administrative_actions', JSON, nullable=True)
    failure_details = Column('failure_details', JSON, nullable=True)
    lustre_configuration = Column('lustre_configuration', JSON, nullable=True)
    network_interface_ids = Column('network_interface_ids', JSON, nullable=True)
    ontap_configuration = Column('ontap_configuration', JSON, nullable=True)
    open_zfs_configuration = Column('open_zfs_configuration', JSON, nullable=True)
    subnet_ids = Column('subnet_ids', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    windows_configuration = Column('windows_configuration', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    file_system_type = Column('file_system_type', Text, nullable=True)
    lifecycle = Column('lifecycle', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    dns_name = Column('dns_name', Text, nullable=True)
    file_system_type_version = Column('file_system_type_version', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    file_system_id = Column('file_system_id', Text, nullable=True)
    storage_type = Column('storage_type', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)