from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSsmPatchBaseline(Base, FormatMixins):
    __tablename__ = 'aws_ssm_patch_baseline'
    sources = Column('sources', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    created_date = Column('created_date', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    approved_patches_enable_non_security = Column('approved_patches_enable_non_security', Boolean, nullable=True)
    approval_rules = Column('approval_rules', JSON, nullable=True)
    approved_patches = Column('approved_patches', JSON, nullable=True)
    global_filters = Column('global_filters', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    patch_groups = Column('patch_groups', JSON, nullable=True)
    modified_date = Column('modified_date', TIMESTAMP, nullable=True)
    rejected_patches = Column('rejected_patches', JSON, nullable=True)
    rejected_patches_action = Column('rejected_patches_action', Text, nullable=True)
    baseline_id = Column('baseline_id', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    operating_system = Column('operating_system', Text, nullable=True)
    approved_patches_compliance_level = Column('approved_patches_compliance_level', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)