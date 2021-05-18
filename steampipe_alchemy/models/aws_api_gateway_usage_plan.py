from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsApiGatewayUsagePlan(Base, FormatMixins):
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


# Local materialized view table
class AwsApiGatewayUsagePlanLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_api_gateway_usage_plan_local'
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


cache = select(AwsApiGatewayUsagePlan).select_from(AwsApiGatewayUsagePlan)
create_materialized_view('aws_api_gateway_usage_plan_local', cache, db.metadata_materialized)
