from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayRestApi(Base):
    __tablename__ = 'aws_api_gateway_rest_api'
    name = Column('name', Text, primary_key=True, nullable=True)
    api_id = Column('api_id', Text, nullable=True)
    version = Column('version', Text, nullable=True)
    api_key_source = Column('api_key_source', Text, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    description = Column('description', Text, nullable=True)
    minimum_compression_size = Column('minimum_compression_size', BigInteger, nullable=True)
    policy = Column('policy', JSON, nullable=True)
    policy_std = Column('policy_std', JSON, nullable=True)
    binary_media_types = Column('binary_media_types', JSON, nullable=True)
    endpoint_configuration_types = Column('endpoint_configuration_types', JSON, nullable=True)
    endpoint_configuration_vpc_endpoint_ids = Column('endpoint_configuration_vpc_endpoint_ids', JSON, nullable=True)
    warnings = Column('warnings', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)