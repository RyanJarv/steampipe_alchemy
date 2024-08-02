from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsAthenaQueryExecution(Base, FormatMixins):
    __tablename__ = 'aws_athena_query_execution'
    _ctx = Column('_ctx', JSON, nullable=True)
    execution_parameters = Column('execution_parameters', JSON, nullable=True)
    submission_date_time = Column('submission_date_time', TIMESTAMP, nullable=True)
    completion_date_time = Column('completion_date_time', TIMESTAMP, nullable=True)
    error_type = Column('error_type', BigInteger, nullable=True)
    error_category = Column('error_category', BigInteger, nullable=True)
    retryable = Column('retryable', Boolean, nullable=True)
    data_scanned_in_bytes = Column('data_scanned_in_bytes', BigInteger, nullable=True)
    engine_execution_time_in_millis = Column('engine_execution_time_in_millis', BigInteger, nullable=True)
    query_planning_time_in_millis = Column('query_planning_time_in_millis', BigInteger, nullable=True)
    query_queue_time_in_millis = Column('query_queue_time_in_millis', BigInteger, nullable=True)
    service_processing_time_in_millis = Column('service_processing_time_in_millis', BigInteger, nullable=True)
    total_execution_time_in_millis = Column('total_execution_time_in_millis', BigInteger, nullable=True)
    reused_previous_result = Column('reused_previous_result', Boolean, nullable=True)
    result_reuse_by_age_enabled = Column('result_reuse_by_age_enabled', Boolean, nullable=True)
    result_reuse_by_age_mag_age_in_minutes = Column('result_reuse_by_age_mag_age_in_minutes', BigInteger, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    kms_key = Column('kms_key', Text, nullable=True)
    data_manifest_location = Column('data_manifest_location', Text, nullable=True)
    expected_bucket_owner = Column('expected_bucket_owner', Text, nullable=True)
    output_location = Column('output_location', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    workgroup = Column('workgroup', Text, nullable=True)
    catalog = Column('catalog', Text, nullable=True)
    database = Column('database', Text, nullable=True)
    query = Column('query', Text, nullable=True)
    effective_engine_version = Column('effective_engine_version', Text, nullable=True)
    selected_engine_version = Column('selected_engine_version', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    statement_type = Column('statement_type', Text, nullable=True)
    substatement_type = Column('substatement_type', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    state_change_reason = Column('state_change_reason', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    error_message = Column('error_message', Text, nullable=True)
    s3_acl_option = Column('s3_acl_option', Text, nullable=True)
    encryption_option = Column('encryption_option', Text, nullable=True)