from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsNetworkfirewallFirewallPolicy(Base, FormatMixins):
    __tablename__ = 'aws_networkfirewall_firewall_policy'
    _ctx = Column('_ctx', JSON, nullable=True)
    consumed_stateful_rule_capacity = Column('consumed_stateful_rule_capacity', BigInteger, nullable=True)
    consumed_stateless_rule_capacity = Column('consumed_stateless_rule_capacity', BigInteger, nullable=True)
    last_modified_time = Column('last_modified_time', TIMESTAMP, nullable=True)
    number_of_associations = Column('number_of_associations', BigInteger, nullable=True)
    encryption_configuration = Column('encryption_configuration', JSON, nullable=True)
    firewall_policy = Column('firewall_policy', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    firewall_policy_id = Column('firewall_policy_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    firewall_policy_status = Column('firewall_policy_status', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)