from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayv2DomainName(Base):
    __tablename__ = 'aws_api_gatewayv2_domain_name'
    domain_name = Column('domain_name', Text, nullable=True)
    domain_name_configurations = Column('domain_name_configurations', JSON, nullable=True)
    mutual_tls_authentication = Column('mutual_tls_authentication', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)