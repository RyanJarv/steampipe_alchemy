from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSagemakerApp(Base, FormatMixins):
    __tablename__ = 'aws_sagemaker_app'
    akas = Column('akas', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    last_health_check_timestamp = Column('last_health_check_timestamp', TIMESTAMP, nullable=True)
    resource_spec = Column('resource_spec', JSON, nullable=True)
    last_user_activity_timestamp = Column('last_user_activity_timestamp', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    user_profile_name = Column('user_profile_name', Text, nullable=True)
    app_type = Column('app_type', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    domain_id = Column('domain_id', Text, nullable=True)
    failure_reason = Column('failure_reason', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    name = Column('name', Text, nullable=True)