from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSfnStateMachineExecution(Base, FormatMixins):
    __tablename__ = 'aws_sfn_state_machine_execution'
    _ctx = Column('_ctx', JSON, nullable=True)
    start_date = Column('start_date', TIMESTAMP, nullable=True)
    stop_date = Column('stop_date', TIMESTAMP, nullable=True)
    input_details = Column('input_details', JSON, nullable=True)
    output_details = Column('output_details', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    trace_header = Column('trace_header', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    execution_arn = Column('execution_arn', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    input = Column('input', Text, nullable=True)
    output = Column('output', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    state_machine_arn = Column('state_machine_arn', Text, nullable=True)