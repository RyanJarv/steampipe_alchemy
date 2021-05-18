from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsApiGatewayv2Api(Base, FormatMixins):
    __tablename__ = 'aws_api_gatewayv2_api'
    name = Column('name', Text, primary_key=True, nullable=True)
    api_id = Column('api_id', Text, nullable=True)
    api_endpoint = Column('api_endpoint', Text, nullable=True)
    protocol_type = Column('protocol_type', Text, nullable=True)
    api_key_selection_expression = Column('api_key_selection_expression', Text, nullable=True)
    route_selection_expression = Column('route_selection_expression', Text, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsApiGatewayv2ApiLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_api_gatewayv2_api_local'
    name = Column('name', Text, primary_key=True, nullable=True)
    api_id = Column('api_id', Text, nullable=True)
    api_endpoint = Column('api_endpoint', Text, nullable=True)
    protocol_type = Column('protocol_type', Text, nullable=True)
    api_key_selection_expression = Column('api_key_selection_expression', Text, nullable=True)
    route_selection_expression = Column('route_selection_expression', Text, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsApiGatewayv2Api).select_from(AwsApiGatewayv2Api)
create_materialized_view('aws_api_gatewayv2_api_local', cache, db.metadata_materialized)
