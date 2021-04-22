from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsVpcEip(Base):
    __tablename__ = 'aws_vpc_eip'
    allocation_id = Column('allocation_id', Text, nullable=True)
    public_ip = Column('public_ip', psql.INET, nullable=True)
    public_ipv4_pool = Column('public_ipv4_pool', Text, nullable=True)
    domain = Column('domain', Text, nullable=True)
    association_id = Column('association_id', Text, nullable=True)
    carrier_ip = Column('carrier_ip', Text, nullable=True)
    customer_owned_ip = Column('customer_owned_ip', psql.INET, nullable=True)
    customer_owned_ipv4_pool = Column('customer_owned_ipv4_pool', Text, nullable=True)
    instance_id = Column('instance_id', Text, nullable=True)
    network_border_group = Column('network_border_group', Text, nullable=True)
    network_interface_id = Column('network_interface_id', Text, nullable=True)
    network_interface_owner_id = Column('network_interface_owner_id', Text, nullable=True)
    private_ip_address = Column('private_ip_address', psql.INET, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)