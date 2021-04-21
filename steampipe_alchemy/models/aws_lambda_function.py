from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy import Base

class AwsLambdaFunction(Base):
    __tablename__ = 'aws_lambda_function'
    name = Column(name='name', type_=Text, nullable=True)
    code_sha_256 = Column(name='code_sha_256', type_=Text, nullable=True)
    code_size = Column(name='code_size', type_=BigInteger, nullable=True)
    description = Column(name='description', type_=Text, nullable=True)
    handler = Column(name='handler', type_=Text, nullable=True)
    kms_key_arn = Column(name='kms_key_arn', type_=Text, nullable=True)
    last_modified = Column(name='last_modified', type_=Text, nullable=True)
    timeout = Column(name='timeout', type_=Text, nullable=True)
    version = Column(name='version', type_=Text, nullable=True)
    master_arn = Column(name='master_arn', type_=Text, nullable=True)
    memory_size = Column(name='memory_size', type_=BigInteger, nullable=True)
    revision_id = Column(name='revision_id', type_=Text, nullable=True)
    role = Column(name='role', type_=Text, nullable=True)
    runtime = Column(name='runtime', type_=Text, nullable=True)
    state = Column(name='state', type_=Text, nullable=True)
    state_reason = Column(name='state_reason', type_=Text, nullable=True)
    state_reason_code = Column(name='state_reason_code', type_=Text, nullable=True)
    last_update_status = Column(name='last_update_status', type_=Text, nullable=True)
    last_update_status_reason = Column(name='last_update_status_reason', type_=Text, nullable=True)
    last_update_status_reason_code = Column(name='last_update_status_reason_code', type_=Text, nullable=True)
    vpc_id = Column(name='vpc_id', type_=Text, nullable=True)
    vpc_security_group_ids = Column(name='vpc_security_group_ids', type_=JSON, nullable=True)
    vpc_subnet_ids = Column(name='vpc_subnet_ids', type_=JSON, nullable=True)
    policy = Column(name='policy', type_=JSON, nullable=True)
    policy_std = Column(name='policy_std', type_=JSON, nullable=True)
    arn = Column(name='arn', type_=Text, primary_key=True, nullable=True)
    tags = Column(name='tags', type_=JSON, nullable=True)
    title = Column(name='title', type_=Text, nullable=True)
    akas = Column(name='akas', type_=JSON, nullable=True)
    partition = Column(name='partition', type_=Text, nullable=True)
    region = Column(name='region', type_=Text, nullable=True)
    account_id = Column(name='account_id', type_=Text, nullable=True)