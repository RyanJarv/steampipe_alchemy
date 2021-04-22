from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRdsDbSnapshot(Base):
    __tablename__ = 'aws_rds_db_snapshot'
    db_snapshot_identifier = Column('db_snapshot_identifier', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    type = Column('type', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    allocated_storage = Column('allocated_storage', BigInteger, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    db_instance_identifier = Column('db_instance_identifier', Text, nullable=True)
    dbi_resource_id = Column('dbi_resource_id', Text, nullable=True)
    encrypted = Column('encrypted', Boolean, nullable=True)
    engine = Column('engine', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    iam_database_authentication_enabled = Column('iam_database_authentication_enabled', Boolean, nullable=True)
    instance_create_time = Column('instance_create_time', TIMESTAMP, nullable=True)
    iops = Column('iops', BigInteger, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    license_model = Column('license_model', Text, nullable=True)
    master_user_name = Column('master_user_name', Text, nullable=True)
    option_group_name = Column('option_group_name', Text, nullable=True)
    percent_progress = Column('percent_progress', BigInteger, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    source_db_snapshot_identifier = Column('source_db_snapshot_identifier', Text, nullable=True)
    source_region = Column('source_region', Text, nullable=True)
    storage_type = Column('storage_type', Text, nullable=True)
    tde_credential_arn = Column('tde_credential_arn', Text, nullable=True)
    timezone = Column('timezone', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    db_snapshot_attributes = Column('db_snapshot_attributes', JSON, nullable=True)
    processor_features = Column('processor_features', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)