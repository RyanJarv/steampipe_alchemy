from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsSecurityhubInsight(Base, FormatMixins):
    __tablename__ = 'aws_securityhub_insight'
    filters = Column('filters', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    _ctx = Column('_ctx', JSON, nullable=True)
    name = Column('name', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    group_by_attribute = Column('group_by_attribute', Text, nullable=True)
    title = Column('title', Text, nullable=True)