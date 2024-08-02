from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsNetworkfirewallFirewall(Base, FormatMixins):
    __tablename__ = 'aws_networkfirewall_firewall'
    _ctx = Column('_ctx', JSON, nullable=True)
    delete_protection = Column('delete_protection', Boolean, nullable=True)
    policy_change_protection = Column('policy_change_protection', Boolean, nullable=True)
    subnet_change_protection = Column('subnet_change_protection', Boolean, nullable=True)
    encryption_configuration = Column('encryption_configuration', JSON, nullable=True)
    firewall_status = Column('firewall_status', JSON, nullable=True)
    subnet_mappings = Column('subnet_mappings', JSON, nullable=True)
    logging_configuration = Column('logging_configuration', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    name = Column('name', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    policy_arn = Column('policy_arn', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)