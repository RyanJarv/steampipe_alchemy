from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsEc2LoadBalancerListener(Base, FormatMixins):
    __tablename__ = 'aws_ec2_load_balancer_listener'
    arn = Column('arn', Text, primary_key=True, nullable=True)
    load_balancer_arn = Column('load_balancer_arn', Text, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    protocol = Column('protocol', Text, nullable=True)
    ssl_policy = Column('ssl_policy', Text, nullable=True)
    alpn_policy = Column('alpn_policy', JSON, nullable=True)
    certificates = Column('certificates', JSON, nullable=True)
    default_actions = Column('default_actions', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsEc2LoadBalancerListenerLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_ec2_load_balancer_listener_local'
    arn = Column('arn', Text, primary_key=True, nullable=True)
    load_balancer_arn = Column('load_balancer_arn', Text, nullable=True)
    port = Column('port', BigInteger, nullable=True)
    protocol = Column('protocol', Text, nullable=True)
    ssl_policy = Column('ssl_policy', Text, nullable=True)
    alpn_policy = Column('alpn_policy', JSON, nullable=True)
    certificates = Column('certificates', JSON, nullable=True)
    default_actions = Column('default_actions', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsEc2LoadBalancerListener).select_from(AwsEc2LoadBalancerListener)
create_materialized_view('aws_ec2_load_balancer_listener_local', cache, db.metadata_materialized)
