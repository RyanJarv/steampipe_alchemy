from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayv2DomainName(Base):
    __tablename__ = 'aws_api_gatewayv2_domain_name'
    domain_name = Column(name='domain_name', type_=Text, nullable=True)
    domain_name_configurations = Column(name='domain_name_configurations', type_=JSON, nullable=True)
    mutual_tls_authentication = Column(name='mutual_tls_authentication', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)