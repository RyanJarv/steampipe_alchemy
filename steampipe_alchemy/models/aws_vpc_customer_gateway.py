from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsVpcCustomerGateway(Base):
    __tablename__ = 'aws_vpc_customer_gateway'
    customer_gateway_id = Column(Text, name='customer_gateway_id', nullable=True)
    type = Column(Text, name='type', nullable=True)
    state = Column(Text, name='state', nullable=True)
    bgp_asn = Column(Text, name='bgp_asn', nullable=True)
    certificate_arn = Column(Text, name='certificate_arn', nullable=True)
    device_name = Column(Text, name='device_name', nullable=True)
    ip_address = Column(psql.INET, name='ip_address', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)