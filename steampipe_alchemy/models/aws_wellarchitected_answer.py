from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWellarchitectedAnswer(Base, FormatMixins):
    __tablename__ = 'aws_wellarchitected_answer'
    is_applicable = Column('is_applicable', Boolean, nullable=True)
    milestone_number = Column('milestone_number', BigInteger, nullable=True)
    choice_answers = Column('choice_answers', JSON, nullable=True)
    choices = Column('choices', JSON, nullable=True)
    selected_choices = Column('selected_choices', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    notes = Column('notes', Text, nullable=True)
    pillar_id = Column('pillar_id', Text, nullable=True)
    question_description = Column('question_description', Text, nullable=True)
    question_id = Column('question_id', Text, nullable=True)
    reason = Column('reason', Text, nullable=True)
    risk = Column('risk', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    question_title = Column('question_title', Text, nullable=True)
    lens_alias = Column('lens_alias', Text, nullable=True)
    workload_id = Column('workload_id', Text, nullable=True)
    helpful_resource_display_text = Column('helpful_resource_display_text', Text, nullable=True)
    helpful_resource_url = Column('helpful_resource_url', Text, nullable=True)
    improvement_plan_url = Column('improvement_plan_url', Text, nullable=True)
    lens_arn = Column('lens_arn', Text, nullable=True)