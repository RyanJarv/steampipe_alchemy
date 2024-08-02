from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53HealthCheck(Base, FormatMixins):
    __tablename__ = 'aws_route53_health_check'
    health_check_version = Column('health_check_version', BigInteger, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    cloud_watch_alarm_configuration = Column('cloud_watch_alarm_configuration', JSON, nullable=True)
    health_check_config = Column('health_check_config', JSON, nullable=True)
    health_check_status = Column('health_check_status', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    caller_reference = Column('caller_reference', Text, nullable=True)
    linked_service_principal = Column('linked_service_principal', Text, nullable=True)
    linked_service_description = Column('linked_service_description', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)