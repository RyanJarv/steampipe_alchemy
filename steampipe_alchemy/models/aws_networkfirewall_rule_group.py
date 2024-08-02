from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsNetworkfirewallRuleGroup(Base, FormatMixins):
    __tablename__ = 'aws_networkfirewall_rule_group'
    number_of_associations = Column('number_of_associations', BigInteger, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    consumed_capacity = Column('consumed_capacity', BigInteger, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    capacity = Column('capacity', BigInteger, nullable=True)
    rule_variables = Column('rule_variables', JSON, nullable=True)
    rules_source = Column('rules_source', JSON, nullable=True)
    stateful_rule_options = Column('stateful_rule_options', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    type = Column('type', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    rule_group_id = Column('rule_group_id', Text, nullable=True)
    rule_group_status = Column('rule_group_status', Text, nullable=True)
    rule_group_name = Column('rule_group_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)