from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcSecurityGroupRule(Base):
    __tablename__ = 'aws_vpc_security_group_rule'
    group_name = Column('group_name', Text, nullable=True)
    group_id = Column('group_id', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    ip_protocol = Column('ip_protocol', Text, nullable=True)
    from_port = Column('from_port', BigInteger, nullable=True)
    to_port = Column('to_port', BigInteger, nullable=True)
    cidr_ip = Column('cidr_ip', psql.CIDR, nullable=True)
    cidr_ipv6 = Column('cidr_ipv6', psql.CIDR, nullable=True)
    pair_group_id = Column('pair_group_id', Text, nullable=True)
    pair_group_name = Column('pair_group_name', Text, nullable=True)
    pair_peering_status = Column('pair_peering_status', Text, nullable=True)
    pair_user_id = Column('pair_user_id', Text, nullable=True)
    pair_vpc_id = Column('pair_vpc_id', Text, nullable=True)
    pair_vpc_peering_connection_id = Column('pair_vpc_peering_connection_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)