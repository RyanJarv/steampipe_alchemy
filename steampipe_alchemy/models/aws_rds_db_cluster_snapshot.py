from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRdsDbClusterSnapshot(Base):
    __tablename__ = 'aws_rds_db_cluster_snapshot'
    db_cluster_snapshot_identifier = Column(name='db_cluster_snapshot_identifier', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    db_cluster_identifier = Column(name='db_cluster_identifier', type_=Text, nullable=True)
    create_time = Column(name='create_time', type_=TIMESTAMP, nullable=True)
    allocated_storage = Column(name='allocated_storage', type_=BigInteger, nullable=True)
    cluster_create_time = Column(name='cluster_create_time', type_=TIMESTAMP, nullable=True)
    engine = Column(name='engine', type_=Text, nullable=True)
    engine_version = Column(name='engine_version', type_=Text, nullable=True)
    iam_database_authentication_enabled = Column(name='iam_database_authentication_enabled', type_=Boolean, nullable=True)
    kms_key_id = Column(name='kms_key_id', type_=Text, nullable=True)
    license_model = Column(name='license_model', type_=Text, nullable=True)
    master_user_name = Column(name='master_user_name', type_=Text, nullable=True)
    percent_progress = Column(name='percent_progress', type_=BigInteger, nullable=True)
    port = Column(name='port', type_=BigInteger, nullable=True)
    source_db_cluster_snapshot_arn = Column(name='source_db_cluster_snapshot_arn', type_=Text, nullable=True)
    storage_encrypted = Column(name='storage_encrypted', type_=Boolean, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    availability_zones = Column(name='availability_zones', type_=JSON, nullable=True)
    db_cluster_snapshot_attributes = Column(name='db_cluster_snapshot_attributes', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)