from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRdsDbClusterSnapshot(Base):
    __tablename__ = 'aws_rds_db_cluster_snapshot'
    db_cluster_snapshot_identifier = Column(Text, name='db_cluster_snapshot_identifier', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    type = Column(Text, name='type', nullable=True)
    status = Column(Text, name='status', nullable=True)
    db_cluster_identifier = Column(Text, name='db_cluster_identifier', nullable=True)
    create_time = Column(TIMESTAMP, name='create_time', nullable=True)
    allocated_storage = Column(BigInteger, name='allocated_storage', nullable=True)
    cluster_create_time = Column(TIMESTAMP, name='cluster_create_time', nullable=True)
    engine = Column(Text, name='engine', nullable=True)
    engine_version = Column(Text, name='engine_version', nullable=True)
    iam_database_authentication_enabled = Column(Boolean, name='iam_database_authentication_enabled', nullable=True)
    kms_key_id = Column(Text, name='kms_key_id', nullable=True)
    license_model = Column(Text, name='license_model', nullable=True)
    master_user_name = Column(Text, name='master_user_name', nullable=True)
    percent_progress = Column(BigInteger, name='percent_progress', nullable=True)
    port = Column(BigInteger, name='port', nullable=True)
    source_db_cluster_snapshot_arn = Column(Text, name='source_db_cluster_snapshot_arn', nullable=True)
    storage_encrypted = Column(Boolean, name='storage_encrypted', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    availability_zones = Column(JSON, name='availability_zones', nullable=True)
    db_cluster_snapshot_attributes = Column(JSON, name='db_cluster_snapshot_attributes', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)