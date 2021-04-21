from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSecurityhubProduct(Base):
    __tablename__ = 'aws_securityhub_product'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    product_arn = Column(name='product_arn', type_=Text, nullable=True)
    activation_url = Column(name='activation_url', type_=Text, nullable=True)
    company_name = Column(name='company_name', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    marketplace_url = Column(name='marketplace_url', type_=Text, nullable=True)
    categories = Column(name='categories', type_=JSON, nullable=True)
    integration_types = Column(name='integration_types', type_=JSON, nullable=True)
    product_subscription_resource_policy = Column(name='product_subscription_resource_policy', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)