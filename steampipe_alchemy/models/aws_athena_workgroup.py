from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAthenaWorkgroup(Base, FormatMixins):
    __tablename__ = 'aws_athena_workgroup'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    additional_configuration = Column('additional_configuration', JSON, nullable=True)
    bytes_scanned_cutoff_per_query = Column('bytes_scanned_cutoff_per_query', BigInteger, nullable=True)
    enforce_workgroup_configuration = Column('enforce_workgroup_configuration', Boolean, nullable=True)
    publish_cloudwatch_metrics_enabled = Column('publish_cloudwatch_metrics_enabled', Boolean, nullable=True)
    requester_pays_enabled = Column('requester_pays_enabled', Boolean, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    effective_engine_version = Column('effective_engine_version', Text, nullable=True)
    selected_engine_version = Column('selected_engine_version', Text, nullable=True)
    execution_role = Column('execution_role', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    s3_acl_option = Column('s3_acl_option', Text, nullable=True)
    encryption_option = Column('encryption_option', Text, nullable=True)
    result_configuration_kms_key = Column('result_configuration_kms_key', Text, nullable=True)
    expected_bucket_owner = Column('expected_bucket_owner', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    output_location = Column('output_location', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    customer_content_kms_key = Column('customer_content_kms_key', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)