from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSecurityhubProduct(Base):
    __tablename__ = 'aws_securityhub_product'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    product_arn = Column(Text, name='product_arn', nullable=True)
    activation_url = Column(Text, name='activation_url', nullable=True)
    company_name = Column(Text, name='company_name', nullable=True)
    description = Column(Text, name='description', nullable=True)
    marketplace_url = Column(Text, name='marketplace_url', nullable=True)
    categories = Column(JSON, name='categories', nullable=True)
    integration_types = Column(JSON, name='integration_types', nullable=True)
    product_subscription_resource_policy = Column(JSON, name='product_subscription_resource_policy', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)