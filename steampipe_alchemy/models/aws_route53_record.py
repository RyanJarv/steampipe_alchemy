from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53Record(Base, FormatMixins):
    __tablename__ = 'aws_route53_record'
    records = Column('records', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    alias_target = Column('alias_target', JSON, nullable=True)
    multi_value_answer = Column('multi_value_answer', Boolean, nullable=True)
    geo_location = Column('geo_location', JSON, nullable=True)
    weight = Column('weight', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    traffic_policy_instance_id = Column('traffic_policy_instance_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    ttl = Column('ttl', Text, nullable=True)
    zone_id = Column('zone_id', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    failover = Column('failover', Text, nullable=True)
    health_check_id = Column('health_check_id', Text, nullable=True)
    latency_region = Column('latency_region', Text, nullable=True)
    set_identifier = Column('set_identifier', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)