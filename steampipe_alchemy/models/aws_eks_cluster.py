from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEksCluster(Base):
    __tablename__ = 'aws_eks_cluster'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    created_at = Column(TIMESTAMP, name='created_at', nullable=True)
    version = Column(Text, name='version', nullable=True)
    endpoint = Column(Text, name='endpoint', nullable=True)
    role_arn = Column(Text, name='role_arn', nullable=True)
    encryption_config = Column(JSON, name='encryption_config', nullable=True)
    resources_vpc_config = Column(JSON, name='resources_vpc_config', nullable=True)
    kubernetes_network_config = Column(JSON, name='kubernetes_network_config', nullable=True)
    logging = Column(JSON, name='logging', nullable=True)
    identity = Column(JSON, name='identity', nullable=True)
    status = Column(Text, name='status', nullable=True)
    certificate_authority = Column(JSON, name='certificate_authority', nullable=True)
    platform_version = Column(Text, name='platform_version', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)