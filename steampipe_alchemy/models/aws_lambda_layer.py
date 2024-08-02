from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsLambdaLayer(Base, FormatMixins):
    __tablename__ = 'aws_lambda_layer'
    _ctx = Column('_ctx', JSON, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    compatible_architectures = Column('compatible_architectures', JSON, nullable=True)
    compatible_runtimes = Column('compatible_runtimes', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    layer_name = Column('layer_name', Text, nullable=True)
    layer_arn = Column('layer_arn', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    layer_version_arn = Column('layer_version_arn', Text, nullable=True)
    license_info = Column('license_info', Text, nullable=True)
    region = Column('region', Text, nullable=True)