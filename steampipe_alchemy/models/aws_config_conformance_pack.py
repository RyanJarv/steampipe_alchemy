from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsConfigConformancePack(Base, FormatMixins):
    __tablename__ = 'aws_config_conformance_pack'
    _ctx = Column('_ctx', JSON, nullable=True)
    last_update_requested_time = Column('last_update_requested_time', TIMESTAMP, nullable=True)
    input_parameters = Column('input_parameters', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    delivery_s3_key_prefix = Column('delivery_s3_key_prefix', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    conformance_pack_id = Column('conformance_pack_id', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    delivery_s3_bucket = Column('delivery_s3_bucket', Text, nullable=True)