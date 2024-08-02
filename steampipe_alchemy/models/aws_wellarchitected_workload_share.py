from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWellarchitectedWorkloadShare(Base, FormatMixins):
    __tablename__ = 'aws_wellarchitected_workload_share'
    _ctx = Column('_ctx', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    shared_with = Column('shared_with', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    workload_id = Column('workload_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    permission_type = Column('permission_type', Text, nullable=True)
    share_id = Column('share_id', Text, nullable=True)