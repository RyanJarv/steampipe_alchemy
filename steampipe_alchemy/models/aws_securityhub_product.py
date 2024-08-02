from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSecurityhubProduct(Base, FormatMixins):
    __tablename__ = 'aws_securityhub_product'
    _ctx = Column('_ctx', JSON, nullable=True)
    categories = Column('categories', JSON, nullable=True)
    integration_types = Column('integration_types', JSON, nullable=True)
    product_subscription_resource_policy = Column('product_subscription_resource_policy', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    product_arn = Column('product_arn', Text, nullable=True)
    activation_url = Column('activation_url', Text, nullable=True)
    company_name = Column('company_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    marketplace_url = Column('marketplace_url', Text, nullable=True)