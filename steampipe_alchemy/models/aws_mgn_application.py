from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsMgnApplication(Base, FormatMixins):
    __tablename__ = 'aws_mgn_application'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_date_time = Column('creation_date_time', TIMESTAMP, nullable=True)
    is_archived = Column('is_archived', Boolean, nullable=True)
    last_modified_date_time = Column('last_modified_date_time', TIMESTAMP, nullable=True)
    application_aggregated_status = Column('application_aggregated_status', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    application_id = Column('application_id', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    name = Column('name', Text, nullable=True)
    description = Column('description', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    wave_id = Column('wave_id', Text, nullable=True)