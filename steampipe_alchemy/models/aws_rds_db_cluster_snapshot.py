from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRdsDbClusterSnapshot(Base):
    __tablename__ = 'aws_rds_db_cluster_snapshot'
    db_cluster_snapshot_identifier = Column('db_cluster_snapshot_identifier', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    type = Column('type', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    db_cluster_identifier = Column('db_cluster_identifier', Text, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    allocated_storage = Column('allocated_storage', BigInteger, nullable=True)
    cluster_create_time = Column('cluster_create_time', TIMESTAMP, nullable=True)
    engine = Column('engine', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    iam_database_authentication_enabled = Column('iam_database_authentication_enabled', Boolean, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    license_model = Column('license_model', Text, nullable=True)
    master_user_name = Column('master_user_name', Text, nullable=True)
    percent_progress = Column('percent_progress', BigInteger, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    source_db_cluster_snapshot_arn = Column('source_db_cluster_snapshot_arn', Text, nullable=True)
    storage_encrypted = Column('storage_encrypted', Boolean, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    availability_zones = Column('availability_zones', JSON, nullable=True)
    db_cluster_snapshot_attributes = Column('db_cluster_snapshot_attributes', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)