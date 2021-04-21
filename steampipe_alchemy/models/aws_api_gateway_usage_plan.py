from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayUsagePlan(Base):
    __tablename__ = 'aws_api_gateway_usage_plan'
    name = Column(name='name', type_=Text, nullable=True)
    id = Column(name='id', type_=Text, primary_key=True, nullable=True)
    product_code = Column(name='product_code', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    quota = Column(name='quota', type_=JSON, nullable=True)
    throttle = Column(name='throttle', type_=JSON, nullable=True)
    api_stages = Column(name='api_stages', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)