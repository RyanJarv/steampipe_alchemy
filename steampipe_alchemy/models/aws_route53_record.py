from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsRoute53Record(Base):
    __tablename__ = 'aws_route53_record'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    zone_id = Column(name='zone_id', type_=Text, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    alias_target = Column(name='alias_target', type_=JSON, nullable=True)
    failover = Column(name='failover', type_=Text, nullable=True)
    geo_location = Column(name='geo_location', type_=JSON, nullable=True)
    health_check_id = Column(name='health_check_id', type_=Text, nullable=True)
    multi_value_answer = Column(name='multi_value_answer', type_=Boolean, nullable=True)
    latency_region = Column(name='latency_region', type_=Text, nullable=True)
    records = Column(name='records', type_=JSON, nullable=True)
    set_identifier = Column(name='set_identifier', type_=Text, nullable=True)
    ttl = Column(name='ttl', type_=Text, nullable=True)
    traffic_policy_instance_id = Column(name='traffic_policy_instance_id', type_=Text, nullable=True)
    weight = Column(name='weight', type_=BigInteger, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)