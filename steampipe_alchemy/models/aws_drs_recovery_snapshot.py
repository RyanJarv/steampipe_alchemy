from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDrsRecoverySnapshot(Base, FormatMixins):
    __tablename__ = 'aws_drs_recovery_snapshot'
    ebs_snapshots = Column('ebs_snapshots', JSON, nullable=True)
    expected_timestamp = Column('expected_timestamp', TIMESTAMP, nullable=True)
    timestamp = Column('timestamp', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    source_server_id = Column('source_server_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    snapshot_id = Column('snapshot_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)