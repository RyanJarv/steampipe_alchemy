from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsServicequotasDefaultServiceQuota(Base, FormatMixins):
    __tablename__ = 'aws_servicequotas_default_service_quota'
    _ctx = Column('_ctx', JSON, nullable=True)
    global_quota = Column('global_quota', Boolean, nullable=True)
    adjustable = Column('adjustable', Boolean, nullable=True)
    value = Column('value', BigInteger, nullable=True)
    error_reason = Column('error_reason', JSON, nullable=True)
    period = Column('period', JSON, nullable=True)
    usage_metric = Column('usage_metric', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    quota_code = Column('quota_code', Text, nullable=True)
    quota_arn = Column('quota_arn', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    service_name = Column('service_name', Text, nullable=True)
    service_code = Column('service_code', Text, nullable=True)
    quota_name = Column('quota_name', Text, nullable=True)
    unit = Column('unit', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)