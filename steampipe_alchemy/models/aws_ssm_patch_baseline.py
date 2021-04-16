from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsSsmPatchBaseline(Base):
    __tablename__ = 'aws_ssm_patch_baseline'
    name = Column(Text, name='name', primary_key=True, nullable=True)
    baseline_id = Column(Text, name='baseline_id', nullable=True)
    description = Column(Text, name='description', nullable=True)
    operating_system = Column(Text, name='operating_system', nullable=True)
    created_date = Column(TIMESTAMP, name='created_date', nullable=True)
    modified_date = Column(TIMESTAMP, name='modified_date', nullable=True)
    approved_patches_compliance_level = Column(Text, name='approved_patches_compliance_level', nullable=True)
    approved_patches_enable_non_security = Column(Boolean, name='approved_patches_enable_non_security', nullable=True)
    approval_rules = Column(JSON, name='approval_rules', nullable=True)
    approved_patches = Column(JSON, name='approved_patches', nullable=True)
    global_filters = Column(JSON, name='global_filters', nullable=True)
    patch_groups = Column(JSON, name='patch_groups', nullable=True)
    rejected_patches_action = Column(Text, name='rejected_patches_action', nullable=True)
    rejected_patches = Column(JSON, name='rejected_patches', nullable=True)
    sources = Column(JSON, name='sources', nullable=True)
    tags_src = Column(JSON, name='tags_src', nullable=True)
    title = Column(Text, name='title', nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)