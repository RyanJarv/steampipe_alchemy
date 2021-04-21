from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsApiGatewayRestApi(Base):
    __tablename__ = 'aws_api_gateway_rest_api'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    api_id = Column(name='api_id', type_=Text, nullable=True)
    version = Column(name='version', type_=Text, nullable=True)
    api_key_source = Column(name='api_key_source', type_=Text, nullable=True)
    created_date = Column(name='created_date', type_=TIMESTAMP, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    minimum_compression_size = Column(name='minimum_compression_size', type_=BigInteger, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    binary_media_types = Column(name='binary_media_types', type_=JSON, nullable=True)
    endpoint_configuration_types = Column(name='endpoint_configuration_types', type_=JSON, nullable=True)
    endpoint_configuration_vpc_endpoint_ids = Column(name='endpoint_configuration_vpc_endpoint_ids', type_=JSON, nullable=True)
    warnings = Column(name='warnings', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)