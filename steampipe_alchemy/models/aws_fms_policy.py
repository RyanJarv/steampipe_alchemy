from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsFmsPolicy(Base, FormatMixins):
    __tablename__ = 'aws_fms_policy'
    _ctx = Column('_ctx', JSON, nullable=True)
    exclude_resource_tags = Column('exclude_resource_tags', Boolean, nullable=True)
    remediation_enabled = Column('remediation_enabled', Boolean, nullable=True)
    security_service_policy_data = Column('security_service_policy_data', JSON, nullable=True)
    delete_unused_fm_managed_resources = Column('delete_unused_fm_managed_resources', Boolean, nullable=True)
    exclude_map = Column('exclude_map', JSON, nullable=True)
    include_map = Column('include_map', JSON, nullable=True)
    resource_set_ids = Column('resource_set_ids', JSON, nullable=True)
    resource_tags = Column('resource_tags', JSON, nullable=True)
    resource_type_list = Column('resource_type_list', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    policy_id = Column('policy_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    policy_description = Column('policy_description', Text, nullable=True)
    policy_status = Column('policy_status', Text, nullable=True)
    resource_type = Column('resource_type', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    policy_update_token = Column('policy_update_token', Text, nullable=True)
    policy_name = Column('policy_name', Text, nullable=True)