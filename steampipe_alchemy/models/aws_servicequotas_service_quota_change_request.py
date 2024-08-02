from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsServicequotasServiceQuotaChangeRequest(Base, FormatMixins):
    __tablename__ = 'aws_servicequotas_service_quota_change_request'
    tags = Column('tags', JSON, nullable=True)
    desired_value = Column('desired_value', psql.DOUBLE_PRECISION, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    created = Column('created', TIMESTAMP, nullable=True)
    global_quota = Column('global_quota', Boolean, nullable=True)
    last_updated = Column('last_updated', TIMESTAMP, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    unit = Column('unit', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    service_code = Column('service_code', Text, nullable=True)
    case_id = Column('case_id', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    quota_name = Column('quota_name', Text, nullable=True)
    quota_code = Column('quota_code', Text, nullable=True)
    quota_arn = Column('quota_arn', Text, nullable=True)
    requester = Column('requester', Text, nullable=True)
    service_name = Column('service_name', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)