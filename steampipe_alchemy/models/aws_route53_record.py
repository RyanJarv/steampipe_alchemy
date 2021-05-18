from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsRoute53Record(Base, FormatMixins):
    __tablename__ = 'aws_route53_record'
    name = Column('name', Text, primary_key=True, nullable=True)
    zone_id = Column('zone_id', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    alias_target = Column('alias_target', JSON, nullable=True)
    failover = Column('failover', Text, nullable=True)
    geo_location = Column('geo_location', JSON, nullable=True)
    health_check_id = Column('health_check_id', Text, nullable=True)
    multi_value_answer = Column('multi_value_answer', Boolean, nullable=True)
    latency_region = Column('latency_region', Text, nullable=True)
    records = Column('records', JSON, nullable=True)
    set_identifier = Column('set_identifier', Text, nullable=True)
    ttl = Column('ttl', Text, nullable=True)
    traffic_policy_instance_id = Column('traffic_policy_instance_id', Text, nullable=True)
    weight = Column('weight', BigInteger, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsRoute53RecordLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_route53_record_local'
    name = Column('name', Text, primary_key=True, nullable=True)
    zone_id = Column('zone_id', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    alias_target = Column('alias_target', JSON, nullable=True)
    failover = Column('failover', Text, nullable=True)
    geo_location = Column('geo_location', JSON, nullable=True)
    health_check_id = Column('health_check_id', Text, nullable=True)
    multi_value_answer = Column('multi_value_answer', Boolean, nullable=True)
    latency_region = Column('latency_region', Text, nullable=True)
    records = Column('records', JSON, nullable=True)
    set_identifier = Column('set_identifier', Text, nullable=True)
    ttl = Column('ttl', Text, nullable=True)
    traffic_policy_instance_id = Column('traffic_policy_instance_id', Text, nullable=True)
    weight = Column('weight', BigInteger, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsRoute53Record).select_from(AwsRoute53Record)
create_materialized_view('aws_route53_record_local', cache, db.metadata_materialized)
