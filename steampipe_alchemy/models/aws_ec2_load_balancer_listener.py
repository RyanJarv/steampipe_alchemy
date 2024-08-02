from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2LoadBalancerListener(Base, FormatMixins):
    __tablename__ = 'aws_ec2_load_balancer_listener'
    akas = Column('akas', JSON, nullable=True)
    alpn_policy = Column('alpn_policy', JSON, nullable=True)
    certificates = Column('certificates', JSON, nullable=True)
    default_actions = Column('default_actions', JSON, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    load_balancer_arn = Column('load_balancer_arn', Text, nullable=True)
    protocol = Column('protocol', Text, nullable=True)
    ssl_policy = Column('ssl_policy', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)