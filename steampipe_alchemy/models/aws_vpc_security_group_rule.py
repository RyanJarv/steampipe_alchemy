from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcSecurityGroupRule(Base):
    __tablename__ = 'aws_vpc_security_group_rule'
    group_name = Column(Text, name='group_name', nullable=True)
    group_id = Column(Text, name='group_id', nullable=True)
    type = Column(Text, name='type', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    owner_id = Column(Text, name='owner_id', nullable=True)
    ip_protocol = Column(Text, name='ip_protocol', nullable=True)
    from_port = Column(BigInteger, name='from_port', nullable=True)
    to_port = Column(BigInteger, name='to_port', nullable=True)
    cidr_ip = Column(psql.CIDR, name='cidr_ip', nullable=True)
    cidr_ipv6 = Column(psql.CIDR, name='cidr_ipv6', nullable=True)
    pair_group_id = Column(Text, name='pair_group_id', nullable=True)
    pair_group_name = Column(Text, name='pair_group_name', nullable=True)
    pair_peering_status = Column(Text, name='pair_peering_status', nullable=True)
    pair_user_id = Column(Text, name='pair_user_id', nullable=True)
    pair_vpc_id = Column(Text, name='pair_vpc_id', nullable=True)
    pair_vpc_peering_connection_id = Column(Text, name='pair_vpc_peering_connection_id', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)