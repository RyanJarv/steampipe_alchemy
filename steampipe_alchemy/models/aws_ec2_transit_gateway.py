from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsEc2TransitGateway(Base):
    __tablename__ = 'aws_ec2_transit_gateway'
    transit_gateway_id = Column('transit_gateway_id', Text, nullable=True)
    transit_gateway_arn = Column('transit_gateway_arn', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    owner_id = Column('owner_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    amazon_side_asn = Column('amazon_side_asn', BigInteger, nullable=True)
    association_default_route_table_id = Column('association_default_route_table_id', Text, nullable=True)
    auto_accept_shared_attachments = Column('auto_accept_shared_attachments', Text, nullable=True)
    default_route_table_association = Column('default_route_table_association', Text, nullable=True)
    default_route_table_propagation = Column('default_route_table_propagation', Text, nullable=True)
    dns_support = Column('dns_support', Text, nullable=True)
    multicast_support = Column('multicast_support', Text, nullable=True)
    propagation_default_route_table_id = Column('propagation_default_route_table_id', Text, nullable=True)
    vpn_ecmp_support = Column('vpn_ecmp_support', Text, nullable=True)
    cidr_blocks = Column('cidr_blocks', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)