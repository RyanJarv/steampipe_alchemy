from sqlalchemy import Column
from sqlalchemy.types import JSON, Text, Boolean, TIMESTAMP, BigInteger
from sqlalchemy.dialects import postgresql as psql
from steampipe_alchemy.mixins import FormatMixins

from steampipe_alchemy import Base

class AwsGuarddutyIpset(Base, FormatMixins):
    __tablename__ = 'aws_guardduty_ipset'
    _ctx = Column('_ctx', JSON, nullable=True)
    tags = Column('tags', JSON, nullable=True)
    akas = Column('akas', JSON, nullable=True)
    sp_ctx = Column('sp_ctx', JSON, nullable=True)
    status = Column('status', Text, nullable=True)
    location = Column('location', Text, nullable=True)
    title = Column('title', Text, nullable=True)
    sp_connection_name = Column('sp_connection_name', Text, nullable=True)
    name = Column('name', Text, primary_key=True, nullable=True)
    partition = Column('partition', Text, nullable=True)
    region = Column('region', Text, nullable=True)
    account_id = Column('account_id', Text, nullable=True)
    detector_id = Column('detector_id', Text, nullable=True)
    ipset_id = Column('ipset_id', Text, nullable=True)
    format = Column('format', Text, nullable=True)