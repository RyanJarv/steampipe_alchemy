from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEksCluster(Base):
    __tablename__ = 'aws_eks_cluster'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    created_at = Column(name='created_at', type_=TIMESTAMP, nullable=True)
    version = Column(name='version', type_=Text, nullable=True)
    endpoint = Column(name='endpoint', type_=Text, nullable=True)
    role_arn = Column(name='role_arn', type_=Text, nullable=True)
    encryption_config = Column(name='encryption_config', type_=JSON, nullable=True)
    resources_vpc_config = Column(name='resources_vpc_config', type_=JSON, nullable=True)
    kubernetes_network_config = Column(name='kubernetes_network_config', type_=JSON, nullable=True)
    logging = Column(name='logging', type_=JSON, nullable=True)
    identity = Column(name='identity', type_=JSON, nullable=True)
    status = Column(name='status', type_=Text, nullable=True)
    certificate_authority = Column(name='certificate_authority', type_=JSON, nullable=True)
    platform_version = Column(name='platform_version', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)