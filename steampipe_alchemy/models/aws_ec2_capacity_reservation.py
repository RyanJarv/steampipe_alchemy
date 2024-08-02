from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2CapacityReservation(Base, FormatMixins):
    __tablename__ = 'aws_ec2_capacity_reservation'
    available_instance_count = Column('available_instance_count', BigInteger, nullable=True)
    total_instance_count = Column('total_instance_count', BigInteger, nullable=True)
    capacity_allocations = Column('capacity_allocations', JSON, nullable=True)
    tag_src = Column('tag_src', JSON, nullable=True)
    ephemeral_storage = Column('ephemeral_storage', Boolean, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    create_date = Column('create_date', TIMESTAMP, nullable=True)
    ebs_optimized = Column('ebs_optimized', Boolean, nullable=True)
    end_date = Column('end_date', TIMESTAMP, nullable=True)
    start_date = Column('start_date', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    capacity_reservation_arn = Column('capacity_reservation_arn', Text, nullable=True)
    instance_type = Column('instance_type', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    availability_zone_id = Column('availability_zone_id', Text, nullable=True)
    end_date_type = Column('end_date_type', Text, nullable=True)
    instance_match_criteria = Column('instance_match_criteria', Text, nullable=True)
    instance_platform = Column('instance_platform', Text, nullable=True)
    capacity_reservation_id = Column('capacity_reservation_id', Text, nullable=True)
    tenancy = Column('tenancy', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)