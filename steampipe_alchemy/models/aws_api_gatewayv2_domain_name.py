from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsApiGatewayv2DomainName(Base):
    __tablename__ = 'aws_api_gatewayv2_domain_name'
    domain_name = Column(Text, name='domain_name', nullable=True)
    domain_name_configurations = Column(JSON, name='domain_name_configurations', nullable=True)
    mutual_tls_authentication = Column(JSON, name='mutual_tls_authentication', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)