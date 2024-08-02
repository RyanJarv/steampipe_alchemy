from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGlueDevEndpoint(Base, FormatMixins):
    __tablename__ = 'aws_glue_dev_endpoint'
    public_keys = Column('public_keys', JSON, nullable=True)
    security_group_ids = Column('security_group_ids', JSON, nullable=True)
    created_timestamp = Column('created_timestamp', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    number_of_nodes = Column('number_of_nodes', BigInteger, nullable=True)
    number_of_workers = Column('number_of_workers', BigInteger, nullable=True)
    last_modified_timestamp = Column('last_modified_timestamp', TIMESTAMP, nullable=True)
    zeppelin_remote_spark_interpreter_port = Column('zeppelin_remote_spark_interpreter_port', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    public_address = Column('public_address', Text, nullable=True)
    public_key = Column('public_key', Text, nullable=True)
    endpoint_name = Column('endpoint_name', Text, nullable=True)
    security_configuration = Column('security_configuration', Text, nullable=True)
    subnet_id = Column('subnet_id', Text, nullable=True)
    vpc_id = Column('vpc_id', Text, nullable=True)
    worker_type = Column('worker_type', Text, nullable=True)
    yarn_endpoint_address = Column('yarn_endpoint_address', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    availability_zone = Column('availability_zone', Text, nullable=True)
    extra_jars_s3_path = Column('extra_jars_s3_path', Text, nullable=True)
    extra_python_libs_s3_path = Column('extra_python_libs_s3_path', Text, nullable=True)
    failure_reason = Column('failure_reason', Text, nullable=True)
    glue_version = Column('glue_version', Text, nullable=True)
    last_update_status = Column('last_update_status', Text, nullable=True)
    private_address = Column('private_address', Text, nullable=True)