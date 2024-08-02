from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsWellarchitectedLensReview(Base, FormatMixins):
    __tablename__ = 'aws_wellarchitected_lens_review'
    _ctx = Column('_ctx', JSON, nullable=True)
    milestone_number = Column('milestone_number', BigInteger, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    pillar_review_summaries = Column('pillar_review_summaries', JSON, nullable=True)
    risk_counts = Column('risk_counts', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    notes = Column('notes', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    lens_name = Column('lens_name', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    lens_arn = Column('lens_arn', Text, nullable=True)
    lens_alias = Column('lens_alias', Text, nullable=True)
    workload_id = Column('workload_id', Text, nullable=True)
    lens_status = Column('lens_status', Text, nullable=True)
    lens_version = Column('lens_version', Text, nullable=True)