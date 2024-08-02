from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsKmsAlias(Base, FormatMixins):
    __tablename__ = 'aws_kms_alias'
    _ctx = Column('_ctx', JSON, nullable=True)
    creation_date = Column('creation_date', TIMESTAMP, nullable=True)
    last_updated_date = Column('last_updated_date', TIMESTAMP, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    title = Column('title', Text, nullable=True)
    alias_name = Column('alias_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    arn = Column('arn', Text, primary_key=True, nullable=True)
    target_key_id = Column('target_key_id', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)