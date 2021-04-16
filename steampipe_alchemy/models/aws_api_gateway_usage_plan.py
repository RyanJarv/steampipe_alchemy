from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsApiGatewayUsagePlan(Base):
    __tablename__ = 'aws_api_gateway_usage_plan'
    name = Column(Text, name='name', nullable=True)
    id = Column(Text, name='id', primary_key=True, nullable=True)
    product_code = Column(Text, name='product_code', nullable=True)
    description = Column(Text, name='description', nullable=True)
    quota = Column(JSON, name='quota', nullable=True)
    throttle = Column(JSON, name='throttle', nullable=True)
    api_stages = Column(JSON, name='api_stages', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)