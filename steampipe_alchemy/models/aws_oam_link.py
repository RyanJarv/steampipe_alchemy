from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsOamLink(Base, FormatMixins):
    __tablename__ = 'aws_oam_link'
    _ctx = Column('_ctx', JSON, nullable=True)
    resource_types = Column('resource_types', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    id = Column('id', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    sink_arn = Column('sink_arn', Text, nullable=True)
    label = Column('label', Text, nullable=True)
    label_template = Column('label_template', Text, nullable=True)