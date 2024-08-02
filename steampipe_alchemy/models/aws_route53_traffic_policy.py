from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsRoute53TrafficPolicy(Base, FormatMixins):
    __tablename__ = 'aws_route53_traffic_policy'
    _ctx = Column('_ctx', JSON, nullable=True)
    version = Column('version', BigInteger, nullable=True)
    document = Column('document', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    name = Column('name', Text, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    id = Column('id', Text, primary_key=True, nullable=True)
    type = Column('type', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    comment = Column('comment', Text, nullable=True)