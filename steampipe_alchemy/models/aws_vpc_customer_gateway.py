from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcCustomerGateway(Base):
    __tablename__ = 'aws_vpc_customer_gateway'
    customer_gateway_id = Column('customer_gateway_id', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    bgp_asn = Column('bgp_asn', Text, nullable=True)
    certificate_arn = Column('certificate_arn', Text, nullable=True)
    device_name = Column('device_name', Text, nullable=True)
    ip_address = Column('ip_address', psql.INET, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)