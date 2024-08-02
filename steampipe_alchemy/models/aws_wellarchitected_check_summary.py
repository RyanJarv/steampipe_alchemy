from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWellarchitectedCheckSummary(Base, FormatMixins):
    __tablename__ = 'aws_wellarchitected_check_summary'
    _ctx = Column('_ctx', JSON, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    account_summary = Column('account_summary', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    name = Column('name', Text, nullable=True)
    pillar_id = Column('pillar_id', Text, nullable=True)
    provider = Column('provider', Text, nullable=True)
    question_id = Column('question_id', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    workload_id = Column('workload_id', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    choice_id = Column('choice_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    lens_arn = Column('lens_arn', Text, nullable=True)