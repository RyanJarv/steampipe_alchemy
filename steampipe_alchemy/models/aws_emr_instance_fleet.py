from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEmrInstanceFleet(Base, FormatMixins):
    __tablename__ = 'aws_emr_instance_fleet'
    _ctx = Column('_ctx', JSON, nullable=True)
    provisioned_on_demand_capacity = Column('provisioned_on_demand_capacity', BigInteger, nullable=True)
    provisioned_spot_capacity = Column('provisioned_spot_capacity', BigInteger, nullable=True)
    target_on_demand_capacity = Column('target_on_demand_capacity', BigInteger, nullable=True)
    target_spot_capacity = Column('target_spot_capacity', BigInteger, nullable=True)
    instance_type_specifications = Column('instance_type_specifications', JSON, nullable=True)
    launch_specifications = Column('launch_specifications', JSON, nullable=True)
    state_change_reason = Column('state_change_reason', JSON, nullable=True)
    status_timeline = Column('status_timeline', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    cluster_id = Column('cluster_id', Text, nullable=True)
    instance_fleet_type = Column('instance_fleet_type', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)