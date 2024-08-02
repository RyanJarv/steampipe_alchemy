from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDocdbClusterSnapshot(Base, FormatMixins):
    __tablename__ = 'aws_docdb_cluster_snapshot'
    storage_encrypted = Column('storage_encrypted', Boolean, nullable=True)
    include_public = Column('include_public', Boolean, nullable=True)
    availability_zones = Column('availability_zones', JSON, nullable=True)
    db_cluster_snapshot_attributes = Column('db_cluster_snapshot_attributes', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    snapshot_create_time = Column('snapshot_create_time', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    cluster_create_time = Column('cluster_create_time', TIMESTAMP, nullable=True)
    percent_progress = Column('percent_progress', BigInteger, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    include_shared = Column('include_shared', Boolean, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    source_db_cluster_snapshot_arn = Column('source_db_cluster_snapshot_arn', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    snapshot_type = Column('snapshot_type', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    db_cluster_identifier = Column('db_cluster_identifier', Text, nullable=True)
    engine = Column('engine', Text, nullable=True)
    engine_version = Column('engine_version', Text, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    master_user_name = Column('master_user_name', Text, nullable=True)
    db_cluster_snapshot_identifier = Column('db_cluster_snapshot_identifier', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)