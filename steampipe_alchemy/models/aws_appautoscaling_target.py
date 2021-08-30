from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAppautoscalingTarget(Base, FormatMixins):
    __tablename__ = 'aws_appautoscaling_target'
    min_capacity = Column('min_capacity', BigInteger, nullable=True)
    max_capacity = Column('max_capacity', BigInteger, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    suspended_state = Column('suspended_state', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    service_namespace = Column('service_namespace', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)
    scalable_dimension = Column('scalable_dimension', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)