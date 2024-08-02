from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDmsReplicationTask(Base, FormatMixins):
    __tablename__ = 'aws_dms_replication_task'
    replication_task_start_date = Column('replication_task_start_date', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    replication_task_creation_date = Column('replication_task_creation_date', TIMESTAMP, nullable=True)
    replication_task_settings = Column('replication_task_settings', JSON, nullable=True)
    replication_task_stats = Column('replication_task_stats', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    status = Column('status', Text, nullable=True)
    stop_reason = Column('stop_reason', Text, nullable=True)
    table_mappings = Column('table_mappings', Text, nullable=True)
    replication_task_identifier = Column('replication_task_identifier', Text, nullable=True)
    target_replication_instance_arn = Column('target_replication_instance_arn', Text, nullable=True)
    task_data = Column('task_data', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    target_endpoint_arn = Column('target_endpoint_arn', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cdc_start_position = Column('cdc_start_position', Text, nullable=True)
    cdc_stop_position = Column('cdc_stop_position', Text, nullable=True)
    last_failure_message = Column('last_failure_message', Text, nullable=True)
    migration_type = Column('migration_type', Text, nullable=True)
    recovery_checkpoint = Column('recovery_checkpoint', Text, nullable=True)
    replication_instance_arn = Column('replication_instance_arn', Text, nullable=True)
    source_endpoint_arn = Column('source_endpoint_arn', Text, nullable=True)