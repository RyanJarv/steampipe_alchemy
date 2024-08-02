from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2ReservedInstance(Base, FormatMixins):
    __tablename__ = 'aws_ec2_reserved_instance'
    usage_price = Column('usage_price', psql.DOUBLE_PRECISION, nullable=True)
    reserved_instances_modifications = Column('reserved_instances_modifications', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    end_time = Column('end_time', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    fixed_price = Column('fixed_price', psql.DOUBLE_PRECISION, nullable=True)
    instance_count = Column('instance_count', BigInteger, nullable=True)
    duration = Column('duration', BigInteger, nullable=True)
    start_time = Column('start_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    scope = Column('scope', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    instance_state = Column('instance_state', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    currency_code = Column('currency_code', Text, nullable=True)
    instance_tenancy = Column('instance_tenancy', Text, nullable=True)
    offering_class = Column('offering_class', Text, nullable=True)
    offering_type = Column('offering_type', Text, nullable=True)
    product_description = Column('product_description', Text, nullable=True)
    reserved_instance_id = Column('reserved_instance_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)