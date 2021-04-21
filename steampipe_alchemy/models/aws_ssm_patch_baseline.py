from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsSsmPatchBaseline(Base):
    __tablename__ = 'aws_ssm_patch_baseline'
    name = Column(name='name', type_=Text, primary_key=True, nullable=True)
    baseline_id = Column(name='baseline_id', type_=Text, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    operating_system = Column(name='operating_system', type_=Text, nullable=True)
    created_date = Column(name='created_date', type_=TIMESTAMP, nullable=True)
    modified_date = Column(name='modified_date', type_=TIMESTAMP, nullable=True)
    approved_patches_compliance_level = Column(name='approved_patches_compliance_level', type_=Text, nullable=True)
    approved_patches_enable_non_security = Column(name='approved_patches_enable_non_security', type_=Boolean, nullable=True)
    approval_rules = Column(name='approval_rules', type_=JSON, nullable=True)
    approved_patches = Column(name='approved_patches', type_=JSON, nullable=True)
    global_filters = Column(name='global_filters', type_=JSON, nullable=True)
    patch_groups = Column(name='patch_groups', type_=JSON, nullable=True)
    rejected_patches_action = Column(name='rejected_patches_action', type_=Text, nullable=True)
    rejected_patches = Column(name='rejected_patches', type_=JSON, nullable=True)
    sources = Column(name='sources', type_=JSON, nullable=True)
    tags_src = Column(name='tags_src', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)