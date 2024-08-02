from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsLambdaEventSourceMapping(Base, FormatMixins):
    __tablename__ = 'aws_lambda_event_source_mapping'
    _ctx = Column('_ctx', JSON, nullable=True)
    starting_position_timestamp = Column('starting_position_timestamp', TIMESTAMP, nullable=True)
    tumbling_window_in_seconds = Column('tumbling_window_in_seconds', BigInteger, nullable=True)
    function_response_types = Column('function_response_types', JSON, nullable=True)
    source_access_configurations = Column('source_access_configurations', JSON, nullable=True)
    destination_config = Column('destination_config', JSON, nullable=True)
    filter_criteria = Column('filter_criteria', JSON, nullable=True)
    amazon_managed_kafka_event_source_config = Column('amazon_managed_kafka_event_source_config', JSON, nullable=True)
    queues = Column('queues', JSON, nullable=True)
    scaling_config = Column('scaling_config', JSON, nullable=True)
    self_managed_event_source = Column('self_managed_event_source', JSON, nullable=True)
    self_managed_kafka_event_source_config = Column('self_managed_kafka_event_source_config', JSON, nullable=True)
    topics = Column('topics', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    batch_size = Column('batch_size', BigInteger, nullable=True)
    bisect_batch_on_function_error = Column('bisect_batch_on_function_error', Boolean, nullable=True)
    last_modified = Column('last_modified', TIMESTAMP, nullable=True)
    maximum_batching_window_in_seconds = Column('maximum_batching_window_in_seconds', BigInteger, nullable=True)
    maximum_record_age_in_seconds = Column('maximum_record_age_in_seconds', BigInteger, nullable=True)
    maximum_retry_attempts = Column('maximum_retry_attempts', BigInteger, nullable=True)
    parallelization_factor = Column('parallelization_factor', BigInteger, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    function_arn = Column('function_arn', Text, nullable=True)
    function_name = Column('function_name', Text, nullable=True)
    starting_position = Column('starting_position', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    last_processing_result = Column('last_processing_result', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    uuid = Column('uuid', Text, nullable=True)
    state = Column('state', Text, nullable=True)
    state_transition_reason = Column('state_transition_reason', Text, nullable=True)