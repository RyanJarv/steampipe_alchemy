from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcCustomerGateway(Base):
    __tablename__ = 'aws_vpc_customer_gateway'
    customer_gateway_id = Column(name='customer_gateway_id', type_=Text, nullable=True)
    type = Column(name='type', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    bgp_asn = Column(name='bgp_asn', type_=Text, nullable=True)
    certificate_arn = Column(name='certificate_arn', type_=Text, nullable=True)
    device_name = Column(name='device_name', type_=Text, nullable=True)
    ip_address = Column(name='ip_address', type_=psql.INET, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)