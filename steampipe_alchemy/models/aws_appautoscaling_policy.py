from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAppautoscalingPolicy(Base, FormatMixins):
    __tablename__ = 'aws_appautoscaling_policy'
    _ctx = Column('_ctx', JSON, nullable=True)
    target_tracking_scaling_policy_configuration = Column('target_tracking_scaling_policy_configuration', JSON, nullable=True)
    step_scaling_policy_configuration = Column('step_scaling_policy_configuration', JSON, nullable=True)
    alarms = Column('alarms', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    policy_arn = Column('policy_arn', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    policy_name = Column('policy_name', Text, nullable=True)
    service_namespace = Column('service_namespace', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)
    scalable_dimension = Column('scalable_dimension', Text, nullable=True)
    policy_type = Column('policy_type', Text, nullable=True)