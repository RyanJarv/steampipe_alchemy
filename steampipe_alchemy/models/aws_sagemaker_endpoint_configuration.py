from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSagemakerEndpointConfiguration(Base, FormatMixins):
    __tablename__ = 'aws_sagemaker_endpoint_configuration'
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    data_capture_config = Column('data_capture_config', JSON, nullable=True)
    production_variants = Column('production_variants', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    name = Column('name', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    kms_key_id = Column('kms_key_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)