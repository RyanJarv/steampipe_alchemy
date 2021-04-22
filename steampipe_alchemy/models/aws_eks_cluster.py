from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEksCluster(Base):
    __tablename__ = 'aws_eks_cluster'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    version = Column('version', Text, nullable=True)
    endpoint = Column('endpoint', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    encryption_config = Column('encryption_config', JSON, nullable=True)
    resources_vpc_config = Column('resources_vpc_config', JSON, nullable=True)
    kubernetes_network_config = Column('kubernetes_network_config', JSON, nullable=True)
    logging = Column('logging', JSON, nullable=True)
    identity = Column('identity', JSON, nullable=True)
    status = Column('status', Text, nullable=True)
    certificate_authority = Column('certificate_authority', JSON, nullable=True)
    platform_version = Column('platform_version', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)