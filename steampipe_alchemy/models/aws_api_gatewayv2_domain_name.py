from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsApiGatewayv2DomainName(Base, FormatMixins):
    __tablename__ = 'aws_api_gatewayv2_domain_name'
    _ctx = Column('_ctx', JSON, nullable=True)
    domain_name_configurations = Column('domain_name_configurations', JSON, nullable=True)
    mutual_tls_authentication = Column('mutual_tls_authentication', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    api_mapping_selection_expression = Column('api_mapping_selection_expression', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)