from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsWellarchitectedWorkload(Base):
    __tablename__ = 'aws_wellarchitected_workload'
    workload_name = Column(Text, name='workload_name', nullable=True)
    workload_arn = Column(Text, name='workload_arn', nullable=True)
    workload_id = Column(Text, name='workload_id', nullable=True)
    architectural_design = Column(Text, name='architectural_design', nullable=True)
    description = Column(Text, name='description', nullable=True)
    environment = Column(Text, name='environment', nullable=True)
    improvement_status = Column(Text, name='improvement_status', nullable=True)
    industry = Column(Text, name='industry', nullable=True)
    industry_type = Column(Text, name='industry_type', nullable=True)
    is_review_owner_update_acknowledged = Column(Boolean, name='is_review_owner_update_acknowledged', nullable=True)
    notes = Column(Text, name='notes', nullable=True)
    owner = Column(Text, name='owner', nullable=True)
    review_owner = Column(Text, name='review_owner', nullable=True)
    review_restriction_date = Column(TIMESTAMP, name='review_restriction_date', nullable=True)
    share_invitation_id = Column(Text, name='share_invitation_id', nullable=True)
    updated_at = Column(TIMESTAMP, name='updated_at', nullable=True)
    account_ids = Column(JSON, name='account_ids', nullable=True)
    aws_regions = Column(JSON, name='aws_regions', nullable=True)
    lenses = Column(JSON, name='lenses', nullable=True)
    non_aws_regions = Column(JSON, name='non_aws_regions', nullable=True)
    pillar_priorities = Column(JSON, name='pillar_priorities', nullable=True)
    risk_counts = Column(JSON, name='risk_counts', nullable=True)
    title = Column(Text, name='title', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)