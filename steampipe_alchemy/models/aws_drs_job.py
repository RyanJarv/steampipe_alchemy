from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsDrsJob(Base, FormatMixins):
    __tablename__ = 'aws_drs_job'
    akas = Column('akas', JSON, nullable=True)
    end_date_time = Column('end_date_time', TIMESTAMP, nullable=True)
    participating_servers = Column('participating_servers', JSON, nullable=True)
    creation_date_time = Column('creation_date_time', TIMESTAMP, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    initiated_by = Column('initiated_by', Text, nullable=True)
    status = Column('status', Text, nullable=True)
    type = Column('type', Text, nullable=True)
    job_id = Column('job_id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)