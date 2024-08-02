from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsCloudfrontFunction(Base, FormatMixins):
    __tablename__ = 'aws_cloudfront_function'
    _ctx = Column('_ctx', JSON, nullable=True)
    function_config = Column('function_config', JSON, nullable=True)
    function_metadata = Column('function_metadata', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    status = Column('status', Text, nullable=True)
    e_tag = Column('e_tag', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)