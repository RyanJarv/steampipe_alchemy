from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRdsDbSnapshot(Base):
    __tablename__ = 'aws_rds_db_snapshot'
    db_snapshot_identifier = Column(Text, name='db_snapshot_identifier', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    type = Column(Text, name='type', nullable=True)
    status = Column(Text, name='status', nullable=True)
    create_time = Column(TIMESTAMP, name='create_time', nullable=True)
    allocated_storage = Column(BigInteger, name='allocated_storage', nullable=True)
    availability_zone = Column(Text, name='availability_zone', nullable=True)
    db_instance_identifier = Column(Text, name='db_instance_identifier', nullable=True)
    dbi_resource_id = Column(Text, name='dbi_resource_id', nullable=True)
    encrypted = Column(Boolean, name='encrypted', nullable=True)
    engine = Column(Text, name='engine', nullable=True)
    engine_version = Column(Text, name='engine_version', nullable=True)
    iam_database_authentication_enabled = Column(Boolean, name='iam_database_authentication_enabled', nullable=True)
    instance_create_time = Column(TIMESTAMP, name='instance_create_time', nullable=True)
    iops = Column(BigInteger, name='iops', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    license_model = Column(Text, name='license_model', nullable=True)
    master_user_name = Column(Text, name='master_user_name', nullable=True)
    option_group_name = Column(Text, name='option_group_name', nullable=True)
    percent_progress = Column(BigInteger, name='percent_progress', nullable=True)
    port = Column(BigInteger, name='port', nullable=True)
    source_db_snapshot_identifier = Column(Text, name='source_db_snapshot_identifier', nullable=True)
    source_region = Column(Text, name='source_region', nullable=True)
    storage_type = Column(Text, name='storage_type', nullable=True)
    tde_credential_arn = Column(Text, name='tde_credential_arn', nullable=True)
    timezone = Column(Text, name='timezone', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    db_snapshot_attributes = Column(JSON, name='db_snapshot_attributes', nullable=True)
    processor_features = Column(JSON, name='processor_features', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)