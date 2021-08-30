from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWafRateBasedRule(Base, FormatMixins):
    __tablename__ = 'aws_waf_rate_based_rule'
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    predicates = Column('predicates', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    rate_limit = Column('rate_limit', BigInteger, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    rule_id = Column('rule_id', Text, nullable=True)
    metric_name = Column('metric_name', Text, nullable=True)
    rate_key = Column('rate_key', Text, nullable=True)
    title = Column('title', Text, nullable=True)