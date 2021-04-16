from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsLambdaFunction(Base):
    __tablename__ = 'aws_lambda_function'
    name = Column(Text, name='name', nullable=True)
    code_sha_256 = Column(Text, name='code_sha_256', nullable=True)
    code_size = Column(BigInteger, name='code_size', nullable=True)
    description = Column(Text, name='description', nullable=True)
    handler = Column(Text, name='handler', nullable=True)
    kms_key_arn = Column(Text, name='kms_key_arn', nullable=True)
    last_modified = Column(Text, name='last_modified', nullable=True)
    timeout = Column(Text, name='timeout', nullable=True)
    version = Column(Text, name='version', nullable=True)
    master_arn = Column(Text, name='master_arn', nullable=True)
    memory_size = Column(BigInteger, name='memory_size', nullable=True)
    revision_id = Column(Text, name='revision_id', nullable=True)
    role = Column(Text, name='role', nullable=True)
    runtime = Column(Text, name='runtime', nullable=True)
    state = Column(Text, name='state', nullable=True)
    state_reason = Column(Text, name='state_reason', nullable=True)
    state_reason_code = Column(Text, name='state_reason_code', nullable=True)
    last_update_status = Column(Text, name='last_update_status', nullable=True)
    last_update_status_reason = Column(Text, name='last_update_status_reason', nullable=True)
    last_update_status_reason_code = Column(Text, name='last_update_status_reason_code', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    vpc_security_group_ids = Column(JSON, name='vpc_security_group_ids', nullable=True)
    vpc_subnet_ids = Column(JSON, name='vpc_subnet_ids', nullable=True)
    policy = Column(JSON, name='policy', nullable=True)
    policy_std = Column(JSON, name='policy_std', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    tags = Column(JSON, name='tags', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)