from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsServiceDiscoveryInstance(Base, FormatMixins):
    __tablename__ = 'aws_service_discovery_instance'
    _ctx = Column('_ctx', JSON, nullable=True)
    instance_ipv4 = Column('instance_ipv4', psql.INET, nullable=True)
    instance_ipv6 = Column('instance_ipv6', psql.INET, nullable=True)
    instance_port = Column('instance_port', BigInteger, nullable=True)
    attributes = Column('attributes', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    service_id = Column('service_id', Text, nullable=True)
    ec2_instance_id = Column('ec2_instance_id', Text, nullable=True)
    alias_dns_name = Column('alias_dns_name', Text, nullable=True)
    instance_cname = Column('instance_cname', Text, nullable=True)
    init_health_status = Column('init_health_status', Text, nullable=True)