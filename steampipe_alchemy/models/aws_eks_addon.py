from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEksAddon(Base, FormatMixins):
    __tablename__ = 'aws_eks_addon'
    akas = Column('akas', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    health_issues = Column('health_issues', JSON, nullable=True)
    modified_at = Column('modified_at', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cluster_name = Column('cluster_name', Text, nullable=True)
    addon_version = Column('addon_version', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    service_account_role_arn = Column('service_account_role_arn', Text, nullable=True)
    addon_name = Column('addon_name', Text, nullable=True)