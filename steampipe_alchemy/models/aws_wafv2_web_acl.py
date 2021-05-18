from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsWafv2WebAcl(Base, FormatMixins):
    __tablename__ = 'aws_wafv2_web_acl'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    id = Column('id', Text, nullable=True)
    scope = Column('scope', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    capacity = Column('capacity', BigInteger, nullable=True)
    lock_token = Column('lock_token', Text, nullable=True)
    managed_by_firewall_manager = Column('managed_by_firewall_manager', Boolean, nullable=True)
    default_action = Column('default_action', JSON, nullable=True)
    pre_process_firewall_manager_rule_groups = Column('pre_process_firewall_manager_rule_groups', JSON, nullable=True)
    post_process_firewall_manager_rule_groups = Column('post_process_firewall_manager_rule_groups', JSON, nullable=True)
    rules = Column('rules', JSON, nullable=True)
    visibility_config = Column('visibility_config', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# Local materialized view table
class AwsWafv2WebAclLocal(db.BaseEphemeralModels, FormatMixins):
    __tablename__ = 'aws_wafv2_web_acl_local'
    name = Column('name', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    id = Column('id', Text, nullable=True)
    scope = Column('scope', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    capacity = Column('capacity', BigInteger, nullable=True)
    lock_token = Column('lock_token', Text, nullable=True)
    managed_by_firewall_manager = Column('managed_by_firewall_manager', Boolean, nullable=True)
    default_action = Column('default_action', JSON, nullable=True)
    pre_process_firewall_manager_rule_groups = Column('pre_process_firewall_manager_rule_groups', JSON, nullable=True)
    post_process_firewall_manager_rule_groups = Column('post_process_firewall_manager_rule_groups', JSON, nullable=True)
    rules = Column('rules', JSON, nullable=True)
    visibility_config = Column('visibility_config', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


cache = select(AwsWafv2WebAcl).select_from(AwsWafv2WebAcl)
create_materialized_view('aws_wafv2_web_acl_local', cache, db.metadata_materialized)
