from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsConfigRule(Base, FormatMixins):
    __tablename__ = 'aws_config_rule'
    _ctx = Column('_ctx', JSON, nullable=True)
    compliance_by_config_rule = Column('compliance_by_config_rule', JSON, nullable=True)
    evaluation_modes = Column('evaluation_modes', JSON, nullable=True)
    input_parameters = Column('input_parameters', JSON, nullable=True)
    scope = Column('scope', JSON, nullable=True)
    source = Column('source', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    rule_id = Column('rule_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    rule_state = Column('rule_state', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    maximum_execution_frequency = Column('maximum_execution_frequency', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, nullable=True)