from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsMskCluster(Base, FormatMixins):
    __tablename__ = 'aws_msk_cluster'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    cluster_configuration = Column('cluster_configuration', JSON, nullable=True)
    cluster_operation = Column('cluster_operation', JSON, nullable=True)
    provisioned = Column('provisioned', JSON, nullable=True)
    state_info = Column('state_info', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    cluster_name = Column('cluster_name', Text, nullable=True)
    active_operation_arn = Column('active_operation_arn', Text, nullable=True)
    cluster_type = Column('cluster_type', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    current_version = Column('current_version', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)