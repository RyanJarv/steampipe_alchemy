from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDlmLifecyclePolicy(Base, FormatMixins):
    __tablename__ = 'aws_dlm_lifecycle_policy'
    _ctx = Column('_ctx', JSON, nullable=True)
    date_created = Column('date_created', TIMESTAMP, nullable=True)
    date_modified = Column('date_modified', TIMESTAMP, nullable=True)
    policy_details = Column('policy_details', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    state = Column('state', Text, nullable=True)
    status_message = Column('status_message', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    policy_id = Column('policy_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    description = Column('description', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    execution_role_arn = Column('execution_role_arn', Text, nullable=True)
    policy_type = Column('policy_type', Text, nullable=True)