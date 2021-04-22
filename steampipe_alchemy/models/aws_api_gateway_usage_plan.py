from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayUsagePlan(Base):
    __tablename__ = 'aws_api_gateway_usage_plan'
    name = Column('name', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    product_code = Column('product_code', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    quota = Column('quota', JSON, nullable=True)
    throttle = Column('throttle', JSON, nullable=True)
    api_stages = Column('api_stages', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)