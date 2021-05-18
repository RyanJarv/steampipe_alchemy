from sqlalchemy import Column, select
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from sqlalchemy_utils import create_materialized_view

from steampipe_alchemy.mixins import FormatMixins
from steampipe_alchemy import Base, db

class AwsAppautoscalingTarget(Base, FormatMixins):
    __tablename__ = 'aws_appautoscaling_target'
    service_namespace = Column('service_namespace', Text, nullable=True)
    resource_id = Column('resource_id', Text, nullable=True)
    scalable_dimension = Column('scalable_dimension', Text, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    min_capacity = Column('min_capacity', BigInteger, nullable=True)
    max_capacity = Column('max_capacity', BigInteger, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    suspended_state = Column('suspended_state', JSON, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)


# # Local materialized view table
# class AwsAppautoscalingTargetLocal(db.BaseEphemeralModels, FormatMixins):
#     __tablename__ = 'aws_appautoscaling_target_local'
#     service_namespace = Column('service_namespace', Text, nullable=True)
#     resource_id = Column('resource_id', Text, nullable=True)
#     scalable_dimension = Column('scalable_dimension', Text, nullable=True)
#     creation_time = Column('creation_time', TIMESTAMP, nullable=True)
#     min_capacity = Column('min_capacity', BigInteger, nullable=True)
#     max_capacity = Column('max_capacity', BigInteger, nullable=True)
#     role_arn = Column('role_arn', Text, nullable=True)
#     suspended_state = Column('suspended_state', JSON, nullable=True)
#     title = Column('title', Text, primary_key=True, nullable=True)
#     partition = Column('partition', Text, nullable=True)
#     region = Column('region', Text, nullable=True)
#     account_id = Column('account_id', Text, nullable=True)
#
#
# cache = select(AwsAppautoscalingTarget).select_from(AwsAppautoscalingTarget)
# create_materialized_view('aws_appautoscaling_target_local', cache, db.metadata_materialized)
