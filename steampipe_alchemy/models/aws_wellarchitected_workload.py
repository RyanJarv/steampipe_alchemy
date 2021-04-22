from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsWellarchitectedWorkload(Base):
    __tablename__ = 'aws_wellarchitected_workload'
    workload_name = Column('workload_name', Text, nullable=True)
    workload_arn = Column('workload_arn', Text, nullable=True)
    workload_id = Column('workload_id', Text, nullable=True)
    architectural_design = Column('architectural_design', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    environment = Column('environment', Text, nullable=True)
    improvement_status = Column('improvement_status', Text, nullable=True)
    industry = Column('industry', Text, nullable=True)
    industry_type = Column('industry_type', Text, nullable=True)
    is_review_owner_update_acknowledged = Column('is_review_owner_update_acknowledged', Boolean, nullable=True)
    notes = Column('notes', Text, nullable=True)
    owner = Column('owner', Text, nullable=True)
    review_owner = Column('review_owner', Text, nullable=True)
    review_restriction_date = Column('review_restriction_date', TIMESTAMP, nullable=True)
    share_invitation_id = Column('share_invitation_id', Text, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    account_ids = Column('account_ids', JSON, nullable=True)
    aws_regions = Column('aws_regions', JSON, nullable=True)
    lenses = Column('lenses', JSON, nullable=True)
    non_aws_regions = Column('non_aws_regions', JSON, nullable=True)
    pillar_priorities = Column('pillar_priorities', JSON, nullable=True)
    risk_counts = Column('risk_counts', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)