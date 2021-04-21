from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2LoadBalancerListener(Base):
    __tablename__ = 'aws_ec2_load_balancer_listener'
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    load_balancer_arn = Column(name='load_balancer_arn', type_=Text, nullable=True)
    port = Column(name='port', type_=BigInteger, nullable=True)
    protocol = Column(name='protocol', type_=Text, nullable=True)
    ssl_policy = Column(name='ssl_policy', type_=Text, nullable=True)
    alpn_policy = Column(name='alpn_policy', type_=JSON, nullable=True)
    certificates = Column(name='certificates', type_=JSON, nullable=True)
    default_actions = Column(name='default_actions', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)