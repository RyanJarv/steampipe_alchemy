from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsEc2KeyPair(Base, FormatMixins):
    __tablename__ = 'aws_ec2_key_pair'
    _ctx = Column('_ctx', JSON, nullable=True)
    tags_src = Column('tags_src', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    create_time = Column('create_time', TIMESTAMP, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    key_name = Column('key_name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    key_pair_id = Column('key_pair_id', Text, nullable=True)
    key_fingerprint = Column('key_fingerprint', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    title = Column('title', Text, primary_key=True, nullable=True)