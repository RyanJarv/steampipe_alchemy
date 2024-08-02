from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsInspectorFinding(Base, FormatMixins):
    __tablename__ = 'aws_inspector_finding'
    confidence = Column('confidence', BigInteger, nullable=True)
    asset_attributes = Column('asset_attributes', JSON, nullable=True)
    attributes = Column('attributes', JSON, nullable=True)
    failed_items = Column('failed_items', JSON, nullable=True)
    service_attributes = Column('service_attributes', JSON, nullable=True)
    user_attributes = Column('user_attributes', JSON, nullable=True)
    indicator_of_compromise = Column('indicator_of_compromise', Boolean, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    numeric_severity = Column('numeric_severity', psql.DOUBLE_PRECISION, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    schema_version = Column('schema_version', BigInteger, nullable=True)
    updated_at = Column('updated_at', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    severity = Column('severity', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    agent_id = Column('agent_id', Text, nullable=True)
    asset_type = Column('asset_type', Text, nullable=True)
    auto_scaling_group = Column('auto_scaling_group', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    recommendation = Column('recommendation', Text, nullable=True)
    service = Column('service', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)