from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSecurityhubStandardsSubscription(Base, FormatMixins):
    __tablename__ = 'aws_securityhub_standards_subscription'
    _ctx = Column('_ctx', JSON, nullable=True)
    enabled_by_default = Column('enabled_by_default', Boolean, nullable=True)
    standards_input = Column('standards_input', JSON, nullable=True)
    standards_managed_by = Column('standards_managed_by', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    standards_subscription_arn = Column('standards_subscription_arn', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    standards_arn = Column('standards_arn', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    standards_status = Column('standards_status', Text, nullable=True)
    standards_status_reason_code = Column('standards_status_reason_code', Text, nullable=True)