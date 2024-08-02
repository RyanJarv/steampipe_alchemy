from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsApiGatewayDomainName(Base, FormatMixins):
    __tablename__ = 'aws_api_gateway_domain_name'
    akas = Column('akas', JSON, nullable=True)
    endpoint_configuration = Column('endpoint_configuration', JSON, nullable=True)
    mutual_tls_authentication = Column('mutual_tls_authentication', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    certificate_upload_date = Column('certificate_upload_date', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    ownership_verification_certificate_arn = Column('ownership_verification_certificate_arn', Text, nullable=True)
    regional_certificate_arn = Column('regional_certificate_arn', Text, nullable=True)
    regional_certificate_name = Column('regional_certificate_name', Text, nullable=True)
    regional_domain_name = Column('regional_domain_name', Text, nullable=True)
    domain_name = Column('domain_name', Text, nullable=True)
    security_policy = Column('security_policy', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    regional_hosted_zone_id = Column('regional_hosted_zone_id', Text, nullable=True)
    certificate_arn = Column('certificate_arn', Text, nullable=True)
    certificate_name = Column('certificate_name', Text, nullable=True)
    distribution_domain_name = Column('distribution_domain_name', Text, nullable=True)
    distribution_hosted_zone_id = Column('distribution_hosted_zone_id', Text, nullable=True)
    domain_name_status = Column('domain_name_status', Text, nullable=True)
    domain_name_status_message = Column('domain_name_status_message', Text, nullable=True)