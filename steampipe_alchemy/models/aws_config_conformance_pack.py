from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsConfigConformancePack(Base, FormatMixins):
    __tablename__ = 'aws_config_conformance_pack'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    conformance_pack_id = Column('conformance_pack_id', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    delivery_s3_bucket = Column('delivery_s3_bucket', Text, nullable=True)
    delivery_s3_key_prefix = Column('delivery_s3_key_prefix', Text, nullable=True)
    last_update_requested_time = Column('last_update_requested_time', TIMESTAMP, nullable=True)
    input_parameters = Column('input_parameters', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsConfigConformancePackLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_config_conformance_pack_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    conformance_pack_id = Column('conformance_pack_id', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    delivery_s3_bucket = Column('delivery_s3_bucket', Text, nullable=True)
    delivery_s3_key_prefix = Column('delivery_s3_key_prefix', Text, nullable=True)
    last_update_requested_time = Column('last_update_requested_time', TIMESTAMP, nullable=True)
    input_parameters = Column('input_parameters', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsConfigConformancePack).select_from(AwsConfigConformancePack)
create_materialized_view('aws_config_conformance_pack_local', cache, db.metadata_materialized)
