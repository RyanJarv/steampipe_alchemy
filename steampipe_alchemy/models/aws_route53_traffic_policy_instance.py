from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53TrafficPolicyInstance(Base, FormatMixins):
    __tablename__ = 'aws_route53_traffic_policy_instance'
    _ctx = Column('_ctx', JSON, nullable=True)
    traffic_policy_version = Column('traffic_policy_version', BigInteger, nullable=True)
    ttl = Column('ttl', BigInteger, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    traffic_policy_id = Column('traffic_policy_id', Text, nullable=True)
    traffic_policy_type = Column('traffic_policy_type', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    hosted_zone_id = Column('hosted_zone_id', Text, nullable=True)
    message = Column('message', Text, nullable=True)
    state = Column('state', Text, nullable=True)