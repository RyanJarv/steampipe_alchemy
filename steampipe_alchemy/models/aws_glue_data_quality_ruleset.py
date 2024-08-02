from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlueDataQualityRuleset(Base, FormatMixins):
    __tablename__ = 'aws_glue_data_quality_ruleset'
    rule_count = Column('rule_count', BigInteger, nullable=True)
    last_modified_on = Column('last_modified_on', TIMESTAMP, nullable=True)
    target_table = Column('target_table', JSON, nullable=True)
    created_on = Column('created_on', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    rule_set = Column('rule_set', Text, nullable=True)
    database_name = Column('database_name', Text, nullable=True)
    table_name = Column('table_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    recommendation_run_id = Column('recommendation_run_id', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)