from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsWellarchitectedWorkload(Base):
    __tablename__ = 'aws_wellarchitected_workload'
    workload_name = Column(name='workload_name', type_=Text, nullable=True)
    workload_arn = Column(name='workload_arn', type_=Text, nullable=True)
    workload_id = Column(name='workload_id', type_=Text, nullable=True)
    architectural_design = Column(name='architectural_design', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    environment = Column(name='environment', type_=Text, nullable=True)
    improvement_status = Column(name='improvement_status', type_=Text, nullable=True)
    industry = Column(name='industry', type_=Text, nullable=True)
    industry_type = Column(name='industry_type', type_=Text, nullable=True)
    is_review_owner_update_acknowledged = Column(name='is_review_owner_update_acknowledged', type_=Boolean, nullable=True)
    notes = Column(name='notes', type_=Text, nullable=True)
    owner = Column(name='owner', type_=Text, nullable=True)
    review_owner = Column(name='review_owner', type_=Text, nullable=True)
    review_restriction_date = Column(name='review_restriction_date', type_=TIMESTAMP, nullable=True)
    share_invitation_id = Column(name='share_invitation_id', type_=Text, nullable=True)
    updated_at = Column(name='updated_at', type_=TIMESTAMP, nullable=True)
    account_ids = Column(name='account_ids', type_=JSON, nullable=True)
    aws_regions = Column(name='aws_regions', type_=JSON, nullable=True)
    lenses = Column(name='lenses', type_=JSON, nullable=True)
    non_aws_regions = Column(name='non_aws_regions', type_=JSON, nullable=True)
    pillar_priorities = Column(name='pillar_priorities', type_=JSON, nullable=True)
    risk_counts = Column(name='risk_counts', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)