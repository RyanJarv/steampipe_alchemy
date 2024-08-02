from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAuditmanagerFramework(Base, FormatMixins):
    __tablename__ = 'aws_auditmanager_framework'
    controls_count = Column('controls_count', BigInteger, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    last_updated_at = Column('last_updated_at', TIMESTAMP, nullable=True)
    control_sets_count = Column('control_sets_count', BigInteger, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    control_sets = Column('control_sets', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    logo = Column('logo', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    last_updated_by = Column('last_updated_by', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    id = Column('id', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    created_by = Column('created_by', Text, nullable=True)
    compliance_type = Column('compliance_type', Text, nullable=True)
    control_sources = Column('control_sources', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    name = Column('name', Text, nullable=True)