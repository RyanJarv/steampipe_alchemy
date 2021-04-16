from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsConfigConformancePack(Base):
    __tablename__ = 'aws_config_conformance_pack'
    name = Column(Text, name='name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    conformance_pack_id = Column(Text, name='conformance_pack_id', nullable=True)
    created_by = Column(Text, name='created_by', nullable=True)
    delivery_s3_bucket = Column(Text, name='delivery_s3_bucket', nullable=True)
    delivery_s3_key_prefix = Column(Text, name='delivery_s3_key_prefix', nullable=True)
    last_update_requested_time = Column(TIMESTAMP, name='last_update_requested_time', nullable=True)
    input_parameters = Column(JSON, name='input_parameters', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    title = Column(Text, name='title', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)