from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlueJob(Base, FormatMixins):
    __tablename__ = 'aws_glue_job'
    _ctx = Column('_ctx', JSON, nullable=True)
    max_capacity = Column('max_capacity', psql.DOUBLE_PRECISION, nullable=True)
    max_retries = Column('max_retries', BigInteger, nullable=True)
    number_of_workers = Column('number_of_workers', BigInteger, nullable=True)
    timeout = Column('timeout', BigInteger, nullable=True)
    command = Column('command', JSON, nullable=True)
    connections = Column('connections', JSON, nullable=True)
    default_arguments = Column('default_arguments', JSON, nullable=True)
    execution_property = Column('execution_property', JSON, nullable=True)
    job_bookmark = Column('job_bookmark', JSON, nullable=True)
    non_overridable_arguments = Column('non_overridable_arguments', JSON, nullable=True)
    notification_property = Column('notification_property', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    allocated_capacity = Column('allocated_capacity', psql.DOUBLE_PRECISION, nullable=True)
    created_on = Column('created_on', TIMESTAMP, nullable=True)
    last_modified_on = Column('last_modified_on', TIMESTAMP, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    worker_type = Column('worker_type', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    glue_version = Column('glue_version', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    log_uri = Column('log_uri', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    role = Column('role', Text, nullable=True)
    security_configuration = Column('security_configuration', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)