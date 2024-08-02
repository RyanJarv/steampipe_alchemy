from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEksFargateProfile(Base, FormatMixins):
    __tablename__ = 'aws_eks_fargate_profile'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    selectors = Column('selectors', JSON, nullable=True)
    subnets = Column('subnets', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    fargate_profile_name = Column('fargate_profile_name', Text, nullable=True)
    cluster_name = Column('cluster_name', Text, nullable=True)
    fargate_profile_arn = Column('fargate_profile_arn', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    pod_execution_role_arn = Column('pod_execution_role_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    region = Column('region', Text, nullable=True)