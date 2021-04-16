from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsRoute53Record(Base):
    __tablename__ = 'aws_route53_record'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    zone_id = Column(Text, name='zone_id', nullable=True)
    type = Column(Text, name='type', nullable=True)
    alias_target = Column(JSON, name='alias_target', nullable=True)
    failover = Column(Text, name='failover', nullable=True)
    geo_location = Column(JSON, name='geo_location', nullable=True)
    health_check_id = Column(Text, name='health_check_id', nullable=True)
    multi_value_answer = Column(Boolean, name='multi_value_answer', nullable=True)
    latency_region = Column(Text, name='latency_region', nullable=True)
    records = Column(JSON, name='records', nullable=True)
    set_identifier = Column(Text, name='set_identifier', nullable=True)
    ttl = Column(Text, name='ttl', nullable=True)
    traffic_policy_instance_id = Column(Text, name='traffic_policy_instance_id', nullable=True)
    weight = Column(BigInteger, name='weight', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)