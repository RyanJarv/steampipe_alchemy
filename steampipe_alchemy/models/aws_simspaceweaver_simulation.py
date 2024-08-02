from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSimspaceweaverSimulation(Base, FormatMixins):
    __tablename__ = 'aws_simspaceweaver_simulation'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_time = Column('creation_time', TIMESTAMP, nullable=True)
    live_simulation_state = Column('live_simulation_state', JSON, nullable=True)
    logging_configuration = Column('logging_configuration', JSON, nullable=True)
    schema_s3_location = Column('schema_s3_location', JSON, nullable=True)
    target_status = Column('target_status', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    execution_id = Column('execution_id', Text, nullable=True)
    maximum_duration = Column('maximum_duration', Text, nullable=True)
    role_arn = Column('role_arn', Text, nullable=True)
    schema_error = Column('schema_error', Text, nullable=True)
    name = Column('name', Text, nullable=True)