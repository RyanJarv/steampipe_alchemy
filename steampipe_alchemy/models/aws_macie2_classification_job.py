from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsMacie2ClassificationJob(Base, FormatMixins):
    __tablename__ = 'aws_macie2_classification_job'
    _ctx = Column('_ctx', JSON, nullable=True)
    sampling_percentage = Column('sampling_percentage', BigInteger, nullable=True)
    bucket_definitions = Column('bucket_definitions', JSON, nullable=True)
    custom_data_identifier_ids = Column('custom_data_identifier_ids', JSON, nullable=True)
    last_run_error_status = Column('last_run_error_status', JSON, nullable=True)
    s3_job_definition = Column('s3_job_definition', JSON, nullable=True)
    schedule_frequency = Column('schedule_frequency', JSON, nullable=True)
    statistics = Column('statistics', JSON, nullable=True)
    user_paused_details = Column('user_paused_details', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    last_run_time = Column('last_run_time', TIMESTAMP, nullable=True)
    job_id = Column('job_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    job_status = Column('job_status', Text, nullable=True)
    job_type = Column('job_type', Text, nullable=True)
    client_token = Column('client_token', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)