from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsConfigConformancePack(Base):
    __tablename__ = 'aws_config_conformance_pack'
    name = Column(name='name', type_=Text, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    conformance_pack_id = Column(name='conformance_pack_id', type_=Text, nullable=True)
    created_by = Column(name='created_by', type_=Text, nullable=True)
    delivery_s3_bucket = Column(name='delivery_s3_bucket', type_=Text, nullable=True)
    delivery_s3_key_prefix = Column(name='delivery_s3_key_prefix', type_=Text, nullable=True)
    last_update_requested_time = Column(name='last_update_requested_time', type_=TIMESTAMP, nullable=True)
    input_parameters = Column(name='input_parameters', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)