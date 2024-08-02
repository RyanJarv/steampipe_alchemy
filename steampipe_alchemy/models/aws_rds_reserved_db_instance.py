from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRdsReservedDbInstance(Base, FormatMixins):
    __tablename__ = 'aws_rds_reserved_db_instance'
    usage_price = Column('usage_price', psql.DOUBLE_PRECISION, nullable=True)
    recurring_charges = Column('recurring_charges', JSON, nullable=True)
    db_instance_count = Column('db_instance_count', BigInteger, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    multi_az = Column('multi_az', Boolean, nullable=True)
    duration = Column('duration', BigInteger, nullable=True)
    fixed_price = Column('fixed_price', psql.DOUBLE_PRECISION, nullable=True)
    start_time = Column('start_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    product_description = Column('product_description', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    reserved_db_instances_offering_id = Column('reserved_db_instances_offering_id', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    _class = Column('class', Text, nullable=True)
    currency_code = Column('currency_code', Text, nullable=True)
    lease_id = Column('lease_id', Text, nullable=True)
    offering_type = Column('offering_type', Text, nullable=True)
    reserved_db_instance_id = Column('reserved_db_instance_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)