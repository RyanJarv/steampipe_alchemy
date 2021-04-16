from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql

from steampipe_alchemy.base import Base

class AwsLambdaVersion(Base):
    __tablename__ = 'aws_lambda_version'
    version = Column(Text, name='version', nullable=True)
    function_name = Column(Text, name='function_name', nullable=True)
    arn = Column(Text, name='arn', primary_key=True, nullable=True)
    master_arn = Column(Text, name='master_arn', nullable=True)
    state = Column(Text, name='state', nullable=True)
    code_sha_256 = Column(Text, name='code_sha_256', nullable=True)
    code_size = Column(BigInteger, name='code_size', nullable=True)
    description = Column(Text, name='description', nullable=True)
    handler = Column(Text, name='handler', nullable=True)
    last_modified = Column(Text, name='last_modified', nullable=True)
    last_update_status = Column(Text, name='last_update_status', nullable=True)
    last_update_status_reason = Column(Text, name='last_update_status_reason', nullable=True)
    last_update_status_reason_code = Column(Text, name='last_update_status_reason_code', nullable=True)
    memory_size = Column(BigInteger, name='memory_size', nullable=True)
    revision_id = Column(Text, name='revision_id', nullable=True)
    runtime = Column(Text, name='runtime', nullable=True)
    timeout = Column(BigInteger, name='timeout', nullable=True)
    vpc_id = Column(Text, name='vpc_id', nullable=True)
    vpc_security_group_ids = Column(JSON, name='vpc_security_group_ids', nullable=True)
    vpc_subnet_ids = Column(JSON, name='vpc_subnet_ids', nullable=True)
    title = Column(Text, name='title', nullable=True)
    akas = Column(JSON, name='akas', nullable=True)
    partition = Column(Text, name='partition', nullable=True)
    region = Column(Text, name='region', nullable=True)
    account_id = Column(Text, name='account_id', nullable=True)