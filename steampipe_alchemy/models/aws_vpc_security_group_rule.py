from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcSecurityGroupRule(Base):
    __tablename__ = 'aws_vpc_security_group_rule'
    group_name = Column(name='group_name', type_=Text, nullable=True)
    group_id = Column(name='group_id', type_=Text, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    owner_id = Column(name='owner_id', type_=Text, nullable=True)
    ip_protocol = Column(name='ip_protocol', type_=Text, nullable=True)
    from_port = Column(name='from_port', type_=BigInteger, nullable=True)
    to_port = Column(name='to_port', type_=BigInteger, nullable=True)
    cidr_ip = Column(name='cidr_ip', type_=psql.CIDR, nullable=True)
    cidr_ipv6 = Column(name='cidr_ipv6', type_=psql.CIDR, nullable=True)
    pair_group_id = Column(name='pair_group_id', type_=Text, nullable=True)
    pair_group_name = Column(name='pair_group_name', type_=Text, nullable=True)
    pair_peering_status = Column(name='pair_peering_status', type_=Text, nullable=True)
    pair_user_id = Column(name='pair_user_id', type_=Text, nullable=True)
    pair_vpc_id = Column(name='pair_vpc_id', type_=Text, nullable=True)
    pair_vpc_peering_connection_id = Column(name='pair_vpc_peering_connection_id', type_=Text, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)