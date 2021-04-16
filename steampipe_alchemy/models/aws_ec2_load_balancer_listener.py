from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsEc2LoadBalancerListener(Base):
    __tablename__ = 'aws_ec2_load_balancer_listener'
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    load_balancer_arn = Column(Text, name='load_balancer_arn', nullable=True)
    port = Column(BigInteger, name='port', nullable=True)
    protocol = Column(Text, name='protocol', nullable=True)
    ssl_policy = Column(Text, name='ssl_policy', nullable=True)
    alpn_policy = Column(JSON, name='alpn_policy', nullable=True)
    certificates = Column(JSON, name='certificates', nullable=True)
    default_actions = Column(JSON, name='default_actions', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)