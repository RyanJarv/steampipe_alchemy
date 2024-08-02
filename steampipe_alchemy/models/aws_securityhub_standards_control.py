from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSecurityhubStandardsControl(Base, FormatMixins):
    __tablename__ = 'aws_securityhub_standards_control'
    _ctx = Column('_ctx', JSON, nullable=True)
    control_status_updated_at = Column('control_status_updated_at', TIMESTAMP, nullable=True)
    related_requirements = Column('related_requirements', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    description = Column('description', Text, nullable=True)
    disabled_reason = Column('disabled_reason', Text, nullable=True)
    remediation_url = Column('remediation_url', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    control_id = Column('control_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    control_status = Column('control_status', Text, nullable=True)
    severity_rating = Column('severity_rating', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)