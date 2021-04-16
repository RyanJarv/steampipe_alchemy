from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsApiGatewayRestApi(Base):
    __tablename__ = 'aws_api_gateway_rest_api'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    api_id = Column(Text, name='api_id', nullable=True)
    version = Column(Text, name='version', nullable=True)
    api_key_source = Column(Text, name='api_key_source', nullable=True)
    created_date = Column(TIMESTAMP, name='created_date', nullable=True)
    description = Column(Text, name='description', nullable=True)
    minimum_compression_size = Column(BigInteger, name='minimum_compression_size', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    binary_media_types = Column(JSON, name='binary_media_types', nullable=True)
    endpoint_configuration_types = Column(JSON, name='endpoint_configuration_types', nullable=True)
    endpoint_configuration_vpc_endpoint_ids = Column(JSON, name='endpoint_configuration_vpc_endpoint_ids', nullable=True)
    warnings = Column(JSON, name='warnings', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)