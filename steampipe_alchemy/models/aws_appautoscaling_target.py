from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAppautoscalingTarget(Base, FormatMixins):
    __tablename__ = 'aws_appautoscaling_target'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    min_capacity = Column('min_capacity', BigInteger, nullable=True)
    max_capacity = Column('max_capacity', BigInteger, nullable=True)
    suspended_state = Column('suspended_state', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    service_namespace = Column('service_namespace', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)
    scalable_dimension = Column('scalable_dimension', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)